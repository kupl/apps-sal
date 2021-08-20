class UnionFindSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (xroot, yroot) = (self.find(x), self.find(y))
        if xroot == yroot:
            return
        if self.rank[xroot] > self.rank[yroot]:
            self.rank[xroot] += self.rank[yroot]
            self.parent[yroot] = xroot
        else:
            self.rank[yroot] += self.rank[xroot]
            self.parent[xroot] = yroot
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m
        uf = UnionFindSet(n)
        ans = -1
        for (step, idx) in enumerate(arr):
            idx -= 1
            uf.rank[idx] = 1
            for j in (idx - 1, idx + 1):
                if 0 <= j < n:
                    if uf.rank[uf.find(j)] == m:
                        ans = step
                    if uf.rank[j]:
                        uf.union(idx, j)
        return ans
