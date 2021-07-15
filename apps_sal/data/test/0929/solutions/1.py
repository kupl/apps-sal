
from collections import deque

icase=0
if icase==0:
    h,w=list(map(int,input().split()))
    a=[[0]*w for i in range(h)]
    for i in range(h):
        a[i]=list(map(int,input().split()))        
elif icase==1: 
    h,w=2,3
    a=[[1, 2, 3], [0, 1, 1]]
elif icase==2: 
    h,w=3,2
    a=[[1, 0], [2, 1], [1, 0]]
elif icase==3: 
    h,w=1,5
    a=[[9, 9, 9, 9, 9]]


astat=0
im=-1
jm=-1
q=deque()

for i in range(h):
    if i%2==0:
        wst=0
        wed=w
        wpt=1
    else:
        wst=w-1
        wed=-1
        wpt=-1
    for j in range(wst,wed,wpt):
#        print("i,j:",i,j)
        if a[i][j]%2==1 and astat==0:
            astat=1
#            print("A:",im,jm,i,j)
        elif a[i][j]%2==1 and astat==1:
            q.append((im,jm,i,j))
#            print("B:",im,jm,i,j)
            astat=0
        elif a[i][j]%2==0 and astat==0:
            astat=0
#            print("C:",im,jm,i,j)
        elif a[i][j]%2==0 and astat==1:
            astat=1
            q.append((im,jm,i,j))
#            print("D:",im,jm,i,j)
        im=i
        jm=j
        
print((len(q)))
for i in range(len(q)):
    yf,xf,yt,xt=q.popleft()
    stra=str(yf+1)+" "+str(xf+1)+" "+str(yt+1)+" "+str(xt+1)
    print(stra)    

