class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        (pu, pv) = (self.find(u), self.find(v))
        if pu == pv:
            return
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (n, ans) = (len(arr), -1)
        uf = UnionFind(n)
        for (step, i) in enumerate(arr):
            i -= 1
            uf.rank[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.rank[uf.find(j)] == m:
                        ans = step
                    if uf.rank[j]:
                        uf.union(i, j)
        for i in range(n):
            if uf.rank[uf.find(i)] == m:
                return n
        return ans
