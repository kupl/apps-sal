import heapq
N = int(input())
Xs = []
Ys = []
for i in range(N):
    (x, y) = map(int, input().split())
    Xs.append((x, i))
    Ys.append((y, i))
Xs.sort()
Ys.sort()
Edges = []
for i in range(1, N):
    ((x1, v1), (x2, v2)) = (Xs[i - 1], Xs[i])
    Edges.append((abs(x1 - x2), v1, v2))
    ((y1, v1), (y2, v2)) = (Ys[i - 1], Ys[i])
    Edges.append((abs(y1 - y2), v1, v2))


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]


heapq.heapify(Edges)
uf = UnionFind(N)
ans = 0
while Edges:
    (d, a, b) = heapq.heappop(Edges)
    if not uf.same(a, b):
        ans += d
        uf.union(a, b)
print(ans)
