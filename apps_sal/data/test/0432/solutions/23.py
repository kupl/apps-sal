import sys
input = sys.stdin.readline


class Unionfind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        p = x

        while not self.par[p] < 0:
            p = self.par[p]

        while x != p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p

        return p

    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.par[rx] += self.par[ry]
        self.par[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


n = int(input())
c = list(map(int, input().split()))
uf = Unionfind(n)
a = list(map(int, input().split()))

for i in range(n):
    uf.unite(i, a[i] - 1)

roots = set(uf.root(i) for i in range(n))
ans = 0

for r in roots:
    cur = r
    s = {r}

    while True:
        nex = a[cur] - 1

        if nex in s:
            sta = nex
            break

        s.add(nex)
        cur = nex

    add = c[sta]
    cur = sta

    while True:
        nex = a[cur] - 1

        if nex == sta:
            break

        add = min(add, c[nex])
        cur = nex

    ans += add

print(ans)
