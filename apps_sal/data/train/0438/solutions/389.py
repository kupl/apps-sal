class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        class DisjointSet:

            def __init__(self, n):
                self.parent = [-1] * n
                self.size = [0] * n

            def make_set(self, v):
                self.parent[v] = v
                self.size[v] = 1

            def find_set(self, v):
                if self.parent[v] != v:
                    self.parent[v] = self.find_set(self.parent[v])
                return self.parent[v]

            def union_sets(self, a, b):
                a = self.find_set(a)
                b = self.find_set(b)
                if self.size[a] < self.size[b]:
                    a, b = b, a
                self.parent[b] = a
                self.size[a] += self.size[b]

        n = len(arr)
        if n == m:
            return n
        ans = -1
        ds = DisjointSet(n)
        for step, i in enumerate(arr):
            i -= 1
            ds.make_set(i)
            for j in (i - 1, i + 1):
                if 0 <= j <= n - 1 and ds.parent[j] > -1:
                    rep = ds.find_set(j)
                    if ds.size[rep] == m:
                        ans = step
                    ds.union_sets(i, j)
        return ans
