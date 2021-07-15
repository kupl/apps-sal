import sys


class UnionFind:
    def __init__(self, n=0):
        self.d = [-1]*n
        self.u = n

    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        self.u -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.d[self.root(x)]

    def num_union(self):
        return self.u


def c2(n):
    return n*(n-1)//2


N, M = list(map(int, sys.stdin.readline().split()))
E = []
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    a -= 1
    b -= 1
    E.append((a, b))

u = UnionFind(N)
r = c2(N)
result = [r]
for a, b in E[::-1]:
    na = u.size(a)
    nb = u.size(b)
    if u.unite(a, b):
        r -= na*nb
    result.append(r)

for r in result[-2::-1]:
    print(r)

