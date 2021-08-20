import sys
from collections import deque


class UnionFind(object):
    __slots__ = ['nodes']

    def __init__(self, n: int):
        self.nodes = [-1] * n

    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> bool:
        (root_x, root_y, nodes) = (self.find(x), self.find(y), self.nodes)
        if root_x != root_y:
            if nodes[root_x] > nodes[root_y]:
                (root_x, root_y) = (root_y, root_x)
            nodes[root_x] += nodes[root_y]
            nodes[root_y] = root_x
        return root_x != root_y


(n, m) = list(map(int, input().split()))
uf = UnionFind(n)
adj = [[] for _ in range(n)]
for (u, v) in (list(map(int, sys.stdin.readline().split())) for _ in range(m)):
    u = u - 1
    v = v - 1
    adj[u].append(v)
    adj[v].append(u)
    uf.unite(u, v)
g_range = []
visited = [0] * n
for i in range(n):
    if visited[i] or not adj[i]:
        continue
    dq = deque([i])
    visited[i] = 1
    (min_v, max_v) = (i, i)
    v_set = []
    size = 0
    while dq:
        v = dq.popleft()
        min_v = min(min_v, v)
        max_v = max(max_v, v)
        v_set.append(v)
        size += 1
        for dest in adj[v]:
            if visited[dest]:
                continue
            visited[dest] = 1
            dq.append(dest)
    g_range.append((min_v, max_v))
g_range.sort()
ans = 0
checked_max = 0
for (s, t) in g_range:
    if t <= checked_max:
        continue
    for v in range(max(s, checked_max) + 1, t):
        if uf.unite(s, v):
            ans += 1
    checked_max = max(checked_max, t)
print(ans)
