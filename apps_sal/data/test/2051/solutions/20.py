from collections import defaultdict
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

        if rx == ry: return False

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


n, m, k = list(map(int, input().split()))
c = list(map(int, input().split()))
uf = Unionfind(n)

for _ in range(m):
    l, r = list(map(int, input().split()))
    uf.unite(l - 1, r - 1)

cnt = defaultdict(dict)

for i in range(n):
    r = uf.root(i)

    if c[i] not in cnt[r]:
        cnt[r][c[i]] = 1
    else:
        cnt[r][c[i]] += 1

ans = 0

for r in list(cnt.keys()):
    l = list(cnt[r].values())
    ans += sum(l) - max(l)

print(ans)
