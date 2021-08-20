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


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = list(map(lambda x: x - 1, arr))
        n = len(arr)
        now = [0] * n
        ans = -1
        uf = Unionfind(n)
        cnt = [0] * (n + 1)
        for i in range(n):
            p = arr[i]
            now[p] = 1
            cnt[1] += 1
            if p - 1 >= 0 and now[p - 1] == 1:
                cnt[uf.count(p)] -= 1
                cnt[uf.count(p - 1)] -= 1
                uf.unite(p - 1, p)
                cnt[uf.count(p)] += 1
            if p + 1 < n and now[p + 1] == 1:
                cnt[uf.count(p)] -= 1
                cnt[uf.count(p + 1)] -= 1
                uf.unite(p, p + 1)
                cnt[uf.count(p)] += 1
            if cnt[m] > 0:
                ans = i + 1
        return ans
