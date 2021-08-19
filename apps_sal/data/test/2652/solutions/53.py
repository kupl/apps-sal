import heapq


class UnionFind:
    from collections import deque

    def __init__(self, v):
        self.v = v
        self._tree = list(range(v + 1))

    def _root(self, a):
        queue = self.deque()
        while self._tree[a] != a:
            queue.append(a)
            a = self._tree[a]
        while queue:
            index = queue.popleft()
            self._tree[index] = a
        return a

    def union(self, a, b):
        root_a = self._root(a)
        root_b = self._root(b)
        self._tree[root_b] = root_a

    def find(self, a, b):
        return self._root(a) == self._root(b)


N = int(input())
V = []
for i in range(N):
    (s, t) = list(map(int, input().split(' ')))
    V.append((i, s, t))
E = []
vx = sorted(V, key=lambda v: v[1])
for (v1, v2) in zip(vx, vx[1:]):
    (i, x1, y1) = v1
    (j, x2, y2) = v2
    heapq.heappush(E, (abs(x1 - x2), i, j))
vy = sorted(V, key=lambda v: v[2])
for (v1, v2) in zip(vy, vy[1:]):
    (i, x1, y1) = v1
    (j, x2, y2) = v2
    heapq.heappush(E, (abs(y1 - y2), i, j))
uf = UnionFind(N)
cost = 0
while E:
    (c, i, j) = heapq.heappop(E)
    if not uf.find(i, j):
        uf.union(i, j)
        cost += c
print(cost)
