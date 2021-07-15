n,m=list(map(int,input().split()))
d=[0]*n
for i in range(m):
    a,b,c=list(map(int,input().split()))
    d[a-1]-=c
    d[b-1]+=c
ans=0
for i in range(n):
    if d[i]>0: ans+=d[i]
print(ans)

