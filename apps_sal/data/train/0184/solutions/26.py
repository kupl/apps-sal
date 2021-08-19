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


class Solution:

    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        cnt = Counter(list(text))
        uf = Unionfind(n)
        for i in range(n - 1):
            if text[i] == text[i + 1]:
                uf.unite(i, i + 1)
        ans = 0
        for i in range(n):
            ans = max(ans, uf.count(i) + (1 if uf.count(i) < cnt[text[i]] else 0))
        for i in range(n - 2):
            if text[i] == text[i + 2] and text[i] != text[i + 1]:
                total = uf.count(i) + uf.count(i + 2)
                ans = max(ans, total + (1 if total < cnt[text[i]] else 0))
        return ans
