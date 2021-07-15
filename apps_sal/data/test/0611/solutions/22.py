n,m=map(int,input().split())
ans=0
k1=((n-1)*n)//2
if(n%2==0):
    z=n//2
    k2=z**2
else:
    z=n//2
    k2=z*(z+1)
fans=0
f2=0
for i in range(m):
    x,d=map(int,input().split())
    if(d<0):
        ans+=x*n+d*k2
    else:
        ans+=x*n+d*k1

print(ans/n)
