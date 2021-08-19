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


(n, m, k) = map(int, input().split())
g = [[] for _ in range(n)]
uf = UnionFind(n)
for i in range(m):
    (a, b) = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
    uf.union(a - 1, b - 1)
for i in range(k):
    (c, d) = map(int, input().split())
    if uf.same(c - 1, d - 1):
        g[c - 1].append(d - 1)
        g[d - 1].append(c - 1)
ans = [0] * n
for i in range(n):
    ans[i] = uf.size(i) - len(g[i]) - 1
print(*ans)
