from typing import List


class UnionFindSet:

    def __init__(self, n):
        self.parent = list(range(n + 2))
        self.rank = [0] * (n + 2)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        (pa, pb) = (self.find(a), self.find(b))
        if pa == pb:
            return False
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFindSet(n)
        ans = -1
        for (step, idx) in enumerate(arr):
            uf.rank[idx] = 1
            for j in [idx + 1, idx - 1]:
                if uf.rank[uf.find(j)] == m:
                    ans = step
                if uf.rank[j]:
                    uf.union(idx, j)
        for i in range(1, n + 1):
            if uf.rank[uf.find(i)] == m:
                return n
        return ans
