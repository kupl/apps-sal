import sys

sys.setrecursionlimit(10**9)

N = int(input())
X_L = [None] * N
Y_L = [None] * N
for i in range(N):
    _x, _y = list(map(int, input().split()))
    X_L[i] = [_x, i]
    Y_L[i] = [_y, i]


class UnionFind():
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [int(_) for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


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
    _d, _i, _j = tmp_l[_]
    if _i >= N or _j >= N:
        print((_i, _j))
    if UF.same(_i, _j):
        continue
    UF.unite(_i, _j)
    ans += _d

print(ans)
