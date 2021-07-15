n=int(input())
x=[]
y=[]
while n>0:
    n-=1
    s=input()
    a=[int(i) for i in s.split(' ')]
    x.append(a[0])
    y.append(a[1])
kx,ky,xx,yy=0,0,-2000,-2000
dx,dy=0,0
for i in x:
    if xx!=i and kx<2:
        kx+=1
        if xx!=-2000:
            dx=abs(xx-i)
        xx=i
for i in y:
    if yy!=i and ky<2:
        ky+=1
        if yy!=-2000:
            dy=abs(yy-i)
        yy=i
if kx==2 and ky==2:
    SS=dx*dy
    print(SS)
else:
    print(-1)
