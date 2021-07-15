k,n=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=k-l[n-1]+l[0]
for i in range(n-1):
    if l[i+1]-l[i]>=ans:
        ans=l[i+1]-l[i]
print(k-ans)
