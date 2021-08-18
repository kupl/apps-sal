class Solution:
    class UnionFind():
        def __init__(self, n):
            self.parents = list(range(n))
            self.sizes = [0] * n

        def find(self, i):
            if i != self.parents[i]:
                self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

        def union(self, i, j):
            pi = self.find(i)
            pj = self.find(j)

            if pi == pj:
                return

            if self.sizes[pi] > self.sizes[pj]:
                self.parents[pj] = pi
                self.sizes[pi] += self.sizes[pj]
            else:
                self.parents[pi] = pj
                self.sizes[pj] += self.sizes[pi]

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        last_seen = -1
        if n == m:
            return n
        union_find = self.UnionFind(n)

        for step, num in enumerate(arr):
            i = num - 1
            union_find.sizes[i] += 1
            for j in [i - 1, i + 1]:
                if 0 <= j < n:
                    pj = union_find.find(j)
                    if union_find.sizes[pj] == m:
                        last_seen = step
                    if union_find.sizes[pj] > 0:
                        union_find.union(i, pj)
        return last_seen
