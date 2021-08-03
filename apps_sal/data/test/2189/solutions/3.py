from heapq import *

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
out = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    g[v].append(u)
    out[u] += 1

q = [-u for u in range(1, n + 1) if not out[u]]
heapify(q)
r = [0] * (n + 1)
c = n
while q:
    u = -heappop(q)
    r[u] = c
    c -= 1
    for v in g[u]:
        out[v] -= 1
        if not out[v]:
            heappush(q, -v)
print(*r[1:])
