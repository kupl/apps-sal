from collections import Counter as C


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = list(range(self.n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] == x:
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
        self.rank[p] += self.rank[q]
        self.par[q] = p
        self.count -= 1


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    UF = UnionFind(n)
    for i in range(m):
        (a, b) = map(int, input().split())
        UF.unite(a - 1, b - 1)
    if n % 2:
        print('First' if (n * (n - 1) // 2 - m) % 2 else 'Second')
    else:
        for i in range(n):
            UF.find(i)
        c = C(UF.par)
        (x, y) = (c[UF.find(0)], c[UF.find(n - 1)])
        print('First' if x % 2 != y % 2 else 'First' if (n * (n - 1) // 2 - x * y - m) % 2 else 'Second')
