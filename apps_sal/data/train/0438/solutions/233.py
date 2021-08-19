class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]

        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        if m == len(arr):
            return m

        n = len(arr)
        uf = UF(n)

        for step, i in enumerate(arr):
            i -= 1  # because of 1-index
            uf.ranks[i] = 1

            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    # if j's parent to j constintutes a m-length array
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j] > 0:
                        uf.union(i, j)
        return ans
