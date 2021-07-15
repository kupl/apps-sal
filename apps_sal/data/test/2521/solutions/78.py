n=int(input())
a=list(map(int,input().split()))
left=[0]*(2*n+1)
right=[0]*(2*n+1)
now_a=a[:n]
left[n]=sum(now_a)
now_a.sort()
from heapq import heapify,heappop,heappush
heapify(now_a)
for i in range(n,2*n):
  if a[i]>now_a[0]:
    left[i+1]=left[i]+a[i]-now_a[0]
    heappop(now_a)
    heappush(now_a,a[i])
  else:
    left[i+1]=left[i]
b=[-x for x in a]
now_b=b[-n:]
right[n]=sum(now_b)
now_b.sort()
heapify(now_b)
for i in range(n,2*n):
  if b[-i-1]>now_b[0]:
    right[i+1]=right[i]+b[-i-1]-now_b[0]
    heappop(now_b)
    heappush(now_b,b[-i-1])
  else:
    right[i+1]=right[i]
ans=-pow(10,14)
for i in range(n+1):
  ans=max(ans,left[n+i]+right[2*n-i])
print(ans)

