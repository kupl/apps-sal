from math import factorial as fa


class UnionFind():
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
            x, y = y, x

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
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


mod = 998244353
n, wa = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ufg = UnionFind(n)
ufl = UnionFind(n)
for i in range(n - 1):
    for j in range(i + 1, n):
        fl = 1
        fg = 1
        for k in range(n):
            if a[i][k] + a[j][k] > wa:
                fg = 0
                break
        for k in range(n):
            if a[k][i] + a[k][j] > wa:
                fl = 0
                break
        if fg:
            ufg.union(i, j)
        if fl:
            ufl.union(i, j)
sg = 1
sl = 1
for i in ufg.roots():
    sg *= fa(ufg.size(i))
    sg %= mod
for i in ufl.roots():
    sl *= fa(ufl.size(i))
    sl %= mod
print((sl * sg) % mod)
