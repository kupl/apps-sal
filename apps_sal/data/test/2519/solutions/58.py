n,k=map(int,input().split())
p=list(map(int,input().split()))


a=[]
for i in range(n):
    a.append((1+p[i])/2)

total=sum(a[i] for i in range(k))
ans=total

for i in range(0,n-k):
    total=total-a[i]+a[i+k]
    if total>ans:
        ans=total
print(ans)
