W,H,N=map(int,input().split())
l,r,b,t=0,W,0,H
for _ in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        l=max(l,x)
    elif a==2:
        r=min(r,x)
    elif a==3:
        b=max(b,y)
    else:
        t=min(t,y)
if l<r and b<t:
    print((r-l)*(t-b))
else:
    print(0)
