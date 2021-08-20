from collections import Counter


class UnionFind:

    def __init__(self):
        (self.uf, self.rank, self.size) = ({}, {}, {})
        self.roots = set()
        self.size_cnt = Counter()

    def add(self, x):
        if x not in self.uf:
            (self.uf[x], self.rank[x], self.size[x]) = (x, 0, 1)
            self.roots.add(x)
            self.size_cnt[1] += 1

    def find(self, x):
        self.add(x)
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return
        self.size_cnt[self.size[xr]] -= 1
        self.size_cnt[self.size[yr]] -= 1
        if self.rank[xr] <= self.rank[yr]:
            self.uf[xr] = yr
            self.size[yr] += self.size[xr]
            self.size_cnt[self.size[yr]] += 1
            self.rank[yr] += self.rank[xr] == self.rank[yr]
            self.roots.discard(xr)
        else:
            self.uf[yr] = xr
            self.size[xr] += self.size[yr]
            self.size_cnt[self.size[xr]] += 1
            self.roots.discard(yr)


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (uf, ans) = (UnionFind(), -1)
        for (step, i) in enumerate(arr, 1):
            if i not in uf.uf:
                uf.add(i)
            if i - 1 in uf.uf:
                uf.union(i, i - 1)
            if i + 1 in uf.uf:
                uf.union(i, i + 1)
            if uf.size_cnt[m] > 0:
                ans = step
        return ans
