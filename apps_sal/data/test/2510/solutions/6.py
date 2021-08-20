class UnionFind:

    def __init__(self, n):
        self.par = []
        self.rank = []
        for i in range(n):
            self.par.append(i)
            self.rank.append(1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] <= self.rank[y]:
                (x, y) = (y, x)
            self.par[y] = x
            self.rank[x] += self.rank[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.rank[self.find(x)]


(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ans = 0
uf = UnionFind(n)
for (a, b) in ab:
    uf.unite(a - 1, b - 1)
for i in range(n):
    ans = max(ans, uf.size(i))
print(ans)
