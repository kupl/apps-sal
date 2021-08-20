from collections import defaultdict
import math


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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join((f'{r}: {m}' for (r, m) in list(self.all_group_members().items())))


(n, k) = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353


def c_swapable(a, x, y):
    if all((a[i][x] + a[i][y] <= k for i in range(n))):
        return True
    else:
        False


def r_swapable(a, s, t):
    if all((a[s][j] + a[t][j] <= k for j in range(n))):
        return True
    else:
        False


colum = UnionFind(n)
row = UnionFind(n)
for hx in range(n - 1):
    for hy in range(hx + 1, n):
        if c_swapable(a, hx, hy):
            colum.union(hx, hy)
for wx in range(n - 1):
    for wy in range(wx + 1, n):
        if r_swapable(a, wx, wy):
            row.union(wx, wy)
ans = 1
for cg in list(colum.all_group_members().values()):
    ans *= math.factorial(len(cg))
ans %= mod
for rg in list(row.all_group_members().values()):
    ans *= math.factorial(len(rg))
print(ans % mod)
