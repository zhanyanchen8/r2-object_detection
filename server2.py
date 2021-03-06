import socket,os,sys
import numpy as np
from PIL import Image
#import cv2
from test import infer_and_match
#sys.path.append("/Users/lhtlinda/Desktop/rps-cv")
#from play import process
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), int(sys.argv[1])))
sys.path.append("/Users/lhtlinda/Desktop/a/rock-paper-scissor-vision")
# from play import main 
action = int(sys.argv[2])
# 1 stands for detecting people, 2 stands for RockPaperScissors
def send_back(location, classes, box_image, clientsocket):
    shape0=1080
    shape1=1920
    shape2=3
    clientsocket.send(box_image.tobytes())
    
print(socket.gethostbyname(socket.gethostname()))

server_socket.listen(5)
idx=0
print("entering while loop")
while 1:
    
        idx+=1
        #accept connections from outside
        (clientsocket, address) = server_socket.accept()
        #now do something with the clientsocket
        #in this case, we'll pretend this is a threaded server
        print("connected to client")    
        while True:
            size = clientsocket.recv(1024)
            #print(size)
            print("got size")
            
            i=str(size)
            print(i)

            
            
            s=str(i)[2:-1]
            s=int(s)
            shape0=1080
            shape1=1920
            shape2=3
            #print(shape0)
            
            #s=str(shape0)
            #print(s)
            #s=s[2:]
            #s0=int(s[:3])
            #s1=int(s[3:6])
            #shape1=clientsocket.recv(1024)
            #print(shape1)
            #s1=int(shape1)
            #print(s0)
            #print(s1)
            #buf=clientsocket.recv(i)
            #im = Image.frombuffer("RGBA",(s0,s1),buf)
            #c=clientsocket.recv(1024)
            #if not c:
            #    break
            #s=str(size)
            #i=int(size)
            #s0=int(shape0)
            #s1=int(shape1)
            #buf=clientsocket.recv(i)
            #print(type(buf))
            #arr=np.frombuffer(buf,dtype="int32")
            #print(arr.shape)
            #im = Image.frombuffer("RGBA",(s0,s1),buf)
            #im.save("test_images/image4.jpg")
            break
        clientsocket.close()
        print("closed")
        server_socket.listen(10)
        
        (clientsocket, address) = server_socket.accept()
        print("accepted second connection")
        print(clientsocket)
        print(address)
        
        l=0
            

        while l<s:
            if l==0:
                buf=clientsocket.recv(1024)
                l+=len(buf)
            else:
                rec=clientsocket.recv(1024)
                l+=len(rec)
                buf+=rec
            
            #buf=clientsocket.recv(i)
            #print(len(buf))
        arr=np.frombuffer(buf,dtype="uint8")
        print(arr.shape)
        arr=arr.reshape((shape0,shape1,shape2))
        #arr2=arr*255
            #print(arr.shape)
            #print(arr)
            

        im = Image.fromarray(arr)
            #im.show()
        im_path='test_images/image{}.jpg'.format(idx)

        im.save('test_images/image{}.jpg'.format(idx))
        if action == 1:
            (location, classes, box_image) = infer_and_match(im_path)
            send_back(location, classes, box_image, clientsocket)
        elif action == 2:
            image=cv2.imread(im_path)
            res=process(image)
            print("result")
            print(res)
        elif action ==3:
            image=arr
            #image=np.resize(image,(120,160))
            test = Image.fromarray(arr2)
            test.save('test_images/scissor/m{}.png'.format(idx));
            res=main(image)

        
        clientsocket.close()
        print('finished!!')
    

print("exit while loop")


#print(client_socket.getsockname())
#client_socket.connect(("", 5005))
