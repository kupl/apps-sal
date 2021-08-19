import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
DIV = 998244353
A = [list(map(int, readline().split())) for i in range(N)]

# Kの制約がない場合
# どんなに入れ替えても、同じ行・同じ列に存在する数の組み合わせは変わらない
# つまり入れ替え可能な列のペアは限られている
# 行・列に対して、入れ替え可能なペアの通り数を算出し、それを掛け合わせたものが答え

# 行Aと行Bが入れ替え可能で行Bと行Cが入れ替え可能な場合、
# 行Aと行Cが直接入れ替え可能でなくても操作によって行A,行Cは入れ替えることが出来る
# UnionFindで入れ替え可能なもの同士をグルーピングする

# by size
# 0-indexed


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
            # 大きい方にくっつける
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
            # print("行",i,j,"入れ替え可能")
            UF_row.unite(i, j)

row_pat = 1
row_roots = UF_row.get_roots()
for root in row_roots:
    siz = UF_row.get_group_size(root)
    # sizの階乗通り分組み合わせが存在する
    # print("root",root,"siz",siz)
    pat = 1
    for p in range(1, siz + 1):
        pat *= p
        pat %= DIV
    row_pat *= pat
    row_pat %= DIV

# print("row_pat",row_pat)

UF_col = UnionFind(N)

for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                break
        else:
            # print("列",i,j,"入れ替え可能")
            UF_col.unite(i, j)

col_pat = 1
col_roots = UF_col.get_roots()
for root in col_roots:
    siz = UF_col.get_group_size(root)
    # print("root",root,"siz",siz)
    pat = 1
    for p in range(1, siz + 1):
        pat *= p
        pat %= DIV
    col_pat *= pat
    col_pat %= DIV

# print("col_pat",col_pat)

print((row_pat * col_pat) % DIV)
