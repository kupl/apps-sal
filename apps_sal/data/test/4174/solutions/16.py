n,x=map(int,input().split())
l=list(map(int,input().split()))
ans=1
d=0
for i in range(len(l)):
    d=d+l[i]
    if d<=x:
        ans+=1
print(ans)
