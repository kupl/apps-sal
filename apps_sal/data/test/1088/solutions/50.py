from math import factorial
(n, K) = map(int, input().split())
mod = 998244353
cnt1 = 0
A = [list(map(int, input().split())) for _ in range(n)]


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

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


uf1 = UnionFind(n)
uf2 = UnionFind(n)
for i in range(n):
    for j in range(i + 1, n):
        if all((A[i][k] + A[j][k] <= K for k in range(n))):
            uf1.union(i, j)
cnt2 = 0
for i in range(n):
    for j in range(i + 1, n):
        if all((A[k][i] + A[k][j] <= K for k in range(n))):
            uf2.union(i, j)
ans = 1
for u in uf1.roots():
    ans *= factorial(uf1.size(u)) % mod
for u in uf2.roots():
    ans *= factorial(uf2.size(u)) % mod
print(ans % mod)
