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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots_nums(self):
        return [-x for x in self.parents if x < 0]

    def num_roots(self):
        return len([i for i, x in enumerate(self.parents) if x < 0])

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def num_members(self, x):
        return abs(self.parents[self.find(x)])

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


MOD = 998244353


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    __floordiv__ = __truediv__

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )


ans = 1
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
uf_row = UnionFind(N)
uf_col = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                break
        else:
            uf_row.union(i, j)
for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                break
        else:
            uf_col.union(i, j)

fact = [ModInt(1)] * 51

for i in range(1, 51):
    fact[i] = fact[i - 1] * i
for p in uf_row.roots_nums():
    ans *= fact[p]
for p in uf_col.roots_nums():
    ans *= fact[p]
print(ans)
