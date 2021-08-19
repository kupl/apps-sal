class UnionFindSet:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return False
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
            self.ranks[px] += self.ranks[py]
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
            self.ranks[py] += self.ranks[px]
        else:
            self.parents[py] = px
            self.ranks[px] += self.ranks[py]
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        (uf, ans) = (UnionFindSet(len(arr)), -1)
        for (step, idx) in enumerate(arr):
            idx -= 1
            uf.ranks[idx] = 1
            for j in [idx - 1, idx + 1]:
                if 0 <= j < len(arr):
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(idx, j)
        return ans
