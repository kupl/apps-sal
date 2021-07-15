n,k=list(map(int,input().split()))
m=26
d=[0]*m
c=input()
for e in c:
    d[ord(e)-65]+=1
d.sort(reverse=True)
ans=0
res=0
for i in range(m):
    if ans>=k:
        break
    if ans+d[i]<=k:
        ans+=d[i]
        res+=d[i]*d[i]
    else:
        res+=(k-ans)*(k-ans)
        ans=k
print(res)

