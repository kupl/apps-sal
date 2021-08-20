from collections import defaultdict
from heapq import heapify, heappush, heappop
(n, m) = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    d[a].append(b)
L = []
heapify(L)
ans = 0
for remain in range(1, m + 1):
    for reward in d[remain]:
        heappush(L, -reward)
    if len(L):
        ans -= heappop(L)
print(ans)
