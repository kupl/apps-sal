import heapq
import math
N=int(input())
CL=list(map(int, input().split()))
heapq.heapify(CL)
min=heapq.heappop(CL)
pre=min
GCD=min
if N!=1:
  for i in range(N-1):
    now=heapq.heappop(CL)
    GCD=math.gcd(GCD, now-pre)
    pre=now
print(GCD)

