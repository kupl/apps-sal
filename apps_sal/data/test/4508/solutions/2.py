import sys
from collections import deque
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


n = inp()
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = inpl()
    (a, b) = (a - 1, b - 1)
    edges[a].append(b)
    edges[b].append(a)
dist = [-1] * n
dist[0] = 0
pa = [-1] * n
se = set()
pq = []
q = deque()
q.append(0)
while q:
    now = q.popleft()
    for nx in edges[now]:
        if dist[nx] != -1:
            continue
        pa[nx] = now
        dist[nx] = dist[now] + 1
        if dist[nx] > 2:
            se.add(nx)
            pq.append((dist[nx], nx))
        q.append(nx)
pq = pq[::-1]
res = 0
ind = 0
while se:
    (d, v) = pq[ind]
    ind += 1
    if not v in se:
        continue
    res += 1
    pv = pa[v]
    se.discard(pv)
    for nv in edges[pv]:
        se.discard(nv)
print(res)
