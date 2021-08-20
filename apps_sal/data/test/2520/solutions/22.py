(n, m, k) = map(int, input().split())


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [-1 for i in range(self.n)]

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return None
        if p > q:
            (p, q) = (q, p)
        self.par[p] += self.par[q]
        self.par[q] = p

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


UF = UnionFind(n)
f_or_b = [0] * n
for i in range(m):
    (a, b) = map(int, input().split())
    UF.unite(a - 1, b - 1)
    f_or_b[a - 1] += 1
    f_or_b[b - 1] += 1
for i in range(k):
    (c, d) = map(int, input().split())
    if UF.same(c - 1, d - 1):
        f_or_b[c - 1] += 1
        f_or_b[d - 1] += 1
for i in range(n):
    print(UF.size(i) - f_or_b[i] - 1, end=' ')
