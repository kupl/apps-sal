import heapq
from collections import defaultdict

n, m = list(map(int, input().split()))

cnt = defaultdict(list)
for _ in range(n):
    a, b = list(map(int, input().split()))
    cnt[a].append(b)

t = []
heapq.heapify(t)
ans = 0
for i in range(1, m+1):
    for j in cnt[i]:
        heapq.heappush(t, -j)
    if t: ans -= heapq.heappop(t)

print(ans)

