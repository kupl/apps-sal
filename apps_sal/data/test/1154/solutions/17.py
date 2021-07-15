n,h,k=map(int,input().split())
hh=0
ans=0
for x in list(map(int,input().split())):
    if hh+x<=h:
        hh+=x
        ans+=hh//k
        hh%=k
    else:
        ans+=1
        hh=x%k
        ans+=x//k
print(ans+(hh>0))
