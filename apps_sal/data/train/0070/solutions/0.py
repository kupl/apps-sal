from collections import defaultdict
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


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()[:-1]
    uf = Unionfind(n)

    for i in range(n // 2):
        uf.unite(i, n - 1 - i)

    for i in range(n - k):
        uf.unite(i, i + k)

    d = defaultdict(dict)

    for i in range(n):
        if s[i] not in d[uf.root(i)]:
            d[uf.root(i)][s[i]] = 1
        else:
            d[uf.root(i)][s[i]] += 1

    rs = set(uf.root(i) for i in range(n))
    ans = 0

    for r in rs:
        ans += uf.count(r) - max(list(d[r].values()))

    print(ans)
