from heapq import heappop, heapify, heappush
from collections import defaultdict
N, M = list(map(int, input().split()))
d = defaultdict(list)
for i in range(N):
    a, b = list(map(int, input().split()))
    d[a].append(b)
h = []
ans = 0
for i in range(1, M + 1):
    if len(d[i]) != 0:
        for x in d[i]:
            heappush(h, -x)
    if len(h) != 0:
        ans -= heappop(h)
print(ans)
