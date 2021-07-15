from heapq import heappush,heappop,heapify
n=int(input())
a=list(map(int,input().split()))
ans=-float("inf")
l=a[:n]
heapify(l)
t=sum(a[:n])
ls=[t]
for i in range(n,2*n):
    t+=a[i]
    heappush(l,a[i])
    t-=heappop(l)
    ls.append(t)
r=[-i for i in a[2*n:]]
heapify(r)
t=sum(a[2*n:])
rs=[t]
for i in range(2*n-1,n-1,-1):
    t+=a[i]
    heappush(r,-a[i])
    t+=heappop(r)
    rs.append(t)
for i in range(n+1):
    ans=max(ans,ls[i]-rs[-i-1])
print(ans)
