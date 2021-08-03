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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, k = map(int, input().split())
a = []
for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)

u = UnionFind(n)
mod = 998244353

for i in range(n - 1):
    for j in range(i + 1, n):
        ai = a[i]
        aj = a[j]
        bit = False
        aij = [i + j for i, j in zip(ai, aj)]
        if max(aij) <= k:
            bit = True
        if bit:
            u.union(i, j)
ans = 1
for i in u.all_group_members():
    li = len(u.members(i))
    res = 1
    for j in range(1, li + 1):
        res *= j
        res %= mod
    ans *= res

o = UnionFind(n)
mod = 998244353
b = list(map(list, zip(*a)))

for i in range(n - 1):
    for j in range(i + 1, n):
        bi = b[i]
        bj = b[j]
        bit = False
        bij = [i + j for i, j in zip(bi, bj)]
        if max(bij) <= k:
            bit = True
        if bit:
            o.union(i, j)

for i in o.all_group_members():
    li = len(o.members(i))
    res = 1
    for j in range(1, li + 1):
        res *= j
        res %= mod
    ans *= res

print(ans % mod)
