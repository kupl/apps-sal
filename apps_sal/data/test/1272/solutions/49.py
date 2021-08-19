import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


class UnionFind:

    def __init__(self, n):
        """木の初期化をする"""
        self.p = [-1] * n
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        """x の親を返す"""
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        """rankの低い親を高い方のの親にする"""
        if not self.same(x, y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                (x, y) = (y, x)
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.p[x] = y
            self.size[y] += self.size[x]
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)


(n, m) = list(map(int, input().split()))
path = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    path.append((a - 1, b - 1))
d = [0] * m
uf = UnionFind(n)
for i in range(m - 1, -1, -1):
    (a, b) = path[i]
    if not uf.same(a, b):
        d[i] = uf.size[uf.find(a)] * uf.size[uf.find(b)]
    uf.unite(a, b)
s = [0] * (m + 1)
for i in range(m):
    s[i + 1] = s[i] + d[i]
print('\n'.join((str(i) for i in s[1:])))
