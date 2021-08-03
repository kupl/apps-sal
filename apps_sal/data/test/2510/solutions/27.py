class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.siz = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.find(self.par[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.siz[x] += self.siz[y]
        else:
            self.par[x] = y
            self.siz[y] += self.siz[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.siz[self.find(x)]


n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.unite(a, b)

res = 0
for i in range(n):
    res = max(res, uf.size(i))

print(res)
