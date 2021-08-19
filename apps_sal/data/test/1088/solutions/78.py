import sys
readline = sys.stdin.readline
(N, K) = map(int, readline().split())
DIV = 998244353
A = [list(map(int, readline().split())) for i in range(N)]


class UnionFind:
    N = 0
    parent = None
    size = None

    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(self.N)]
        self.size = [1] * self.N

    def root(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]

    def get_group_size(self, x):
        return self.size[self.root(x)]

    def get_roots(self):
        r = set()
        for i in range(self.N):
            r.add(self.root(i))
        return r

    def show_parent(self):
        print(self.parent)

    def show_size(self):
        print(self.size)


UF_row = UnionFind(N)
for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                break
        else:
            UF_row.unite(i, j)
row_pat = 1
row_roots = UF_row.get_roots()
for root in row_roots:
    siz = UF_row.get_group_size(root)
    pat = 1
    for p in range(1, siz + 1):
        pat *= p
        pat %= DIV
    row_pat *= pat
    row_pat %= DIV
UF_col = UnionFind(N)
for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                break
        else:
            UF_col.unite(i, j)
col_pat = 1
col_roots = UF_col.get_roots()
for root in col_roots:
    siz = UF_col.get_group_size(root)
    pat = 1
    for p in range(1, siz + 1):
        pat *= p
        pat %= DIV
    col_pat *= pat
    col_pat %= DIV
print(row_pat * col_pat % DIV)
