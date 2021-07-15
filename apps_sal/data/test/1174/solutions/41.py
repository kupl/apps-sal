import heapq
from collections import deque
n,m=map(int,input().split())
A=list(map(int,input().split()))

for i in range(n):
    A[i]*=-1
heapq.heapify(A)

for i in range(m):
    x=heapq.heappop(A)
    if x%2==0:
        x//=2
    else:
        x=x//2 +1
    heapq.heappush(A,x)

ans=-1*sum(A)
print(ans)
