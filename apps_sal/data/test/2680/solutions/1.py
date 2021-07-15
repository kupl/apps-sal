n,b=list(map(int,input().split()))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x1,y1=1,1
x2,y2=n,1
x3,y3=1,n
x4,y4=n,n
c=0
for i in range(0,b):
    c=c+min(abs(x[i]-x1)+abs(y[i]-y1),abs(x[i]-x2)+abs(y[i]-y2),abs(x[i]-x3)+abs(y[i]-y3),abs(x[i]-x4)+abs(y[i]-y4))
print(c)

