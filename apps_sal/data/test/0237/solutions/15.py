q,w,e=list(map(int,input().split()))
w-=q
z=e-1
x=q-e
z,x=min(z,x),max(z,x)
ans=1
t=1
while (w-t)>=0:
    w-=t
    ans+=1
    if z==x==0:
        ans+=w//t
        break
    if z>0:
        z-=1
        t+=1
    if x>0:
        x-=1
        t+=1
print(ans)

