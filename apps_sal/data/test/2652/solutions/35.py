import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
X_L = [None] * N
Y_L = [None] * N
for i in range(N):
    (_x, _y) = list(map(int, input().split()))
    X_L[i] = [_x, i]
    Y_L[i] = [_y, i]


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

    def unite(self, x, y):
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


X_L.sort()
Y_L.sort()
dx_l = [None] * (N - 1)
dy_l = [None] * (N - 1)
for i in range(N - 1):
    dx_l[i] = [X_L[i + 1][0] - X_L[i][0], X_L[i][1], X_L[i + 1][1]]
    dy_l[i] = [Y_L[i + 1][0] - Y_L[i][0], Y_L[i][1], Y_L[i + 1][1]]
tmp_l = dx_l + dy_l
tmp_l.sort()
UF = UnionFind(N)
ans = 0
for _ in range(2 * N - 2):
    (_d, _i, _j) = tmp_l[_]
    if UF.same(_i, _j):
        continue
    UF.unite(_i, _j)
    ans += _d
print(ans)
