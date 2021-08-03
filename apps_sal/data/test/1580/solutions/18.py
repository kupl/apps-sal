import sys
sys.setrecursionlimit(10**9)


class UnionFind:
    def __init__(self, n):
        self.n = [-1] * n
        self.r = [0] * n
        self.siz = n

    def find_root(self, x):
        if self.n[x] < 0:
            return x
        else:
            self.n[x] = self.find_root(self.n[x])
            return self.n[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.r[x] > self.r[y]:
            self.n[x] += self.n[y]
            self.n[y] = x
        else:
            self.n[y] += self.n[x]
            self.n[x] = y
            if self.r[x] == self.r[y]:
                self.r[y] += 1
        self.siz -= 1

    def root_same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.n[self.find_root(x)]

    def size(self):
        return self.siz


n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    x, y, z = map(int, input().split())
    uf.unite(x - 1, y - 1)
print(uf.size())
