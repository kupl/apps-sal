w,h,n=list(map(int,input().split()))
xmin=0
xmax=w
ymin=0
ymax=h
for i in range(n):
    x,y,a=list(map(int,input().split()))
    if a==1:
        xmin=max(x,xmin)
    elif a==2:
        xmax=min(x,xmax)
    elif a==3:
        ymin=max(y,ymin)
    else:
        ymax=min(y,ymax)
print((max(0,xmax-xmin)*max(0,ymax-ymin)))


