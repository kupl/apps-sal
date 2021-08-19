import math
import heapq
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
lis = []
for i in a:
    lis.append(-1 * i)
heapq.heapify(lis)
for _ in range(m):
    tmp = heapq.heappop(lis)
    heapq.heappush(lis, -1 * (-tmp // 2))
print(-sum(lis))
