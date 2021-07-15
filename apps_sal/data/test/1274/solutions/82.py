from collections import defaultdict
from heapq import heappush, heappop

N, M = list(map(int, input().split()))
jobs = defaultdict(list)
heap = []
ans = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    if a <= M:
        jobs[a].append(b)

for m in range(1, M+1):
    for b in jobs[m]:
        heappush(heap, -b)
    if heap:
        maxb = -heappop(heap)
        ans += maxb
print(ans)


