import heapq
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    d[a].append(b)
    d[b].append(a)
vis = [0] * n
vis[0] = 1
print(1, end=' ')
l = []
for i in d[0]:
    if not vis[i]:
        heapq.heappush(l, i)
        vis[i] = 1
heapq.heapify(l)
while l:
    t = heapq.heappop(l)
    print(t + 1, end=' ')
    for i in d[t]:
        if not vis[i]:
            heapq.heappush(l, i)
            vis[i] = 1
