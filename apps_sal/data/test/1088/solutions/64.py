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


(n, K) = list(map(int, input().split()))
mod = 998244353
a = [list(map(int, input().split())) for i in range(n)]


def factorial_mod(n, mod):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
        ret %= mod
    return ret


uf_ver = UnionFind(n + 1)
for i in range(n):
    for j in range(n):
        is_ok = 1
        for k in range(n):
            if a[i][k] + a[j][k] <= K:
                pass
            else:
                is_ok = 0
                break
        if is_ok:
            uf_ver.union(i, j)
uf_hol = UnionFind(n + 1)
for i in range(n):
    for j in range(n):
        is_ok = 1
        for k in range(n):
            if a[k][i] + a[k][j] <= K:
                pass
            else:
                is_ok = 0
                break
        if is_ok:
            uf_hol.union(i, j)
ans = 1
dic1 = uf_ver.all_group_members()
for v in list(dic1.values()):
    ans *= factorial_mod(len(v), mod)
    ans %= mod
dic2 = uf_hol.all_group_members()
for v in list(dic2.values()):
    ans *= factorial_mod(len(v), mod)
    ans %= mod
print(ans)
