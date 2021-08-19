class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        n = len(arr)
        uf = UnionFind(n)
        ans = -1
        for (step, i) in enumerate(arr):
            index = i - 1
            uf.ranks[index] = 1
            for j in [index - 1, index + 1]:
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(index, j)
        return ans


class UnionFind:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, n1, n2):
        (p1, p2) = (self.find(n1), self.find(n2))
        if p1 == p2:
            return
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
            return
        else:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
            return
