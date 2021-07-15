import math
a,b,c=list(map(int,input().split()))
x1,y1,x2,y2=list(map(int,input().split()))
s=abs(x1-x2)+abs(y1-y2)
if a!=0:
    xk1=-1*(b*y1+c)/a
    xk2=-1*(b*y2+c)/a
else:
    xk1=10**18
    xk2=10**18
if b!=0:
    yk1=-1*(a*x1+c)/b
    yk2=-1*(a*x2+c)/b
else:
    yk1=10**18
    yk2=10**18
lx1=abs(y1-yk1)
lx2=abs(y2-yk2)
ly1=abs(x1-xk1)
ly2=abs(x2-xk2)
s1=math.sqrt((x1-x2)**2+(yk1-yk2)**2)
s2=math.sqrt((x1-xk1)**2+(yk1-y1)**2)
s3=math.sqrt((x1-xk2)**2+(yk1-y2)**2)
s4=math.sqrt((xk1-x2)**2+(y1-yk2)**2)
s5=math.sqrt((x2-xk2)**2+(y2-yk2)**2)
s6=math.sqrt((xk1-xk2)**2+(y1-y2)**2)
s=min(s,lx1+lx2+s1,lx1+s3+ly2,ly1+s4+lx2,ly1+s6+ly2)
print(s)

