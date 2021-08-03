# Union Find Tree
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


N, K = map(int, input().split())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

UF1 = UnionFind(N)
UF2 = UnionFind(N)

for i in range(N):
    for j in range(i + 1, N):
        l = 0
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                l = 1
        if l == 0:
            UF1.union(i, j)

for i in range(N):
    for j in range(i + 1, N):
        l = 0
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                l = 1
        if l == 0:
            UF2.union(i, j)


def fac(x):
    ans = 1
    for i in range(1, x + 1):
        ans *= i
        ans %= 998244353
    return ans


ans = 1
for i in UF1.parents:
    if i < 0:
        ans *= fac(-i)
        ans %= 998244353

for i in UF2.parents:
    if i < 0:
        ans *= fac(-i)
        ans %= 998244353

print(ans)
