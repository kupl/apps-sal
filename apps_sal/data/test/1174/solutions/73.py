n,m=map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    a[i]*=-1

import heapq,math

heapq.heapify(a)

for _ in range(m):
    b=heapq.heappop(a)*(-1)
    b //=2

    heapq.heappush(a,b*(-1))

print(sum(a)*(-1))
