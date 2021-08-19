class UnionSet:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)
        if xParent == yParent:
            return
        if self.rank[xParent] > self.rank[yParent]:
            self.parent[yParent] = xParent
            self.rank[xParent] += self.rank[yParent]
        else:
            self.parent[xParent] = yParent
            self.rank[yParent] += self.rank[xParent]


class Solution:

    def findLatestStep(self, arr, m: int) -> int:
        us = UnionSet(len(arr))
        ans = -1
        for (step, idx) in enumerate(arr):
            idx -= 1
            us.rank[idx] = 1
            for j in (-1, 1):
                neighbour = idx + j
                if 0 <= neighbour < len(arr):
                    if us.rank[us.find(neighbour)] == m:
                        ans = step
                    if us.rank[neighbour]:
                        us.union(neighbour, idx)
        for i in range(len(arr)):
            if us.rank[us.find(i)] == m:
                return len(arr)
        return ans
