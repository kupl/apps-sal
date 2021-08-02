class DisjointSets:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.siz = [1] * n

    def root(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.parent[y] = x
        self.siz[x] += self.siz[y]

    def size(self, x):
        return self.siz[self.root(x)]


n = int(input())
X = []
Y = []
for i in range(n):
    x, y = list(map(int, input().split()))
    X.append((i, x))
    Y.append((i, y))
X.sort(key=lambda x: x[1])
Y.sort(key=lambda y: y[1])
edges = []
for i in range(1, n):
    a, x1 = X[i - 1]
    b, x2 = X[i]
    edges.append((a, b, x2 - x1))
    c, y1 = Y[i - 1]
    d, y2 = Y[i]
    edges.append((c, d, y2 - y1))
edges.sort(key=lambda y: y[2])

ans = 0
ds = DisjointSets(n)
for i in range(2 * n - 2):
    u, v, dist = edges[i]
    if ds.same(u, v):
        continue
    ds.unite(u, v)
    ans += dist
print(ans)
