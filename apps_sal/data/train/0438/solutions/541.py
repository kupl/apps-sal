from collections import Counter


class UnionFind:

    def __init__(self):
        (self.uf, self.rank, self.size, self.cnt) = ({}, {}, {}, Counter())

    def add(self, x):
        if x not in self.uf:
            (self.uf[x], self.rank[x], self.size[x]) = (x, 0, 1)
            self.cnt[1] += 1

    def find(self, x):
        self.add(x)
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return
        self.cnt[self.size[xr]] -= 1
        self.cnt[self.size[yr]] -= 1
        if self.rank[xr] <= self.rank[yr]:
            self.uf[xr] = yr
            self.size[yr] += self.size[xr]
            self.cnt[self.size[yr]] += 1
            self.rank[yr] += self.rank[xr] == self.rank[yr]
        else:
            self.uf[yr] = xr
            self.size[xr] += self.size[yr]
            self.cnt[self.size[xr]] += 1


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UnionFind()
        ans = -1
        for (s, ind) in enumerate(arr):
            if ind not in uf.uf:
                uf.add(ind)
            if ind - 1 in uf.uf:
                uf.union(ind, ind - 1)
            if ind + 1 in uf.uf:
                uf.union(ind, ind + 1)
            if uf.cnt[m] > 0:
                ans = s + 1
        return ans
