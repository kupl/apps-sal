class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        (pu, pv) = (self.find(u), self.find(v))
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFindSet(n)
        b_arr = [0] * n
        ans = -1
        for (step, num) in enumerate(arr):
            idx = num - 1
            b_arr[idx] = 1
            if idx > 0 and b_arr[idx - 1]:
                p = uf.find(idx - 1)
                if uf.ranks[p] == m:
                    ans = step
                uf.union(idx, idx - 1)
            if idx < n - 1 and b_arr[idx + 1]:
                p = uf.find(idx + 1)
                if uf.ranks[p] == m:
                    ans = step
                uf.union(idx, idx + 1)
            p = uf.find(idx)
            if uf.ranks[p] == m:
                ans = step + 1
        for idx in range(n):
            p = uf.find(idx)
            if uf.ranks[p] == m:
                return n
        return ans
