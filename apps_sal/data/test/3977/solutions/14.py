import sys
input = sys.stdin.readline


class Unionfind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        r = x

        while not self.par[r] < 0:
            r = self.par[r]

        t = x

        while t != r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r

        return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return

        if self.rank[rx] <= self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry

            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


n, m, k = map(int, input().split())
c = list(map(int, input().split()))
uf = Unionfind(n)

for _ in range(m):
    u, v = map(int, input().split())
    uf.unite(u - 1, v - 1)

sizes = [uf.count(ci - 1) for ci in c]
sizes.sort()
sizes[-1] += n - sum(sizes)
ans = 0

for size in sizes:
    ans += size * (size - 1) // 2

ans -= m

print(ans)
