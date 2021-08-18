

class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        self.parents[max(pu, pv)] = min(pu, pv)
        self.ranks[min(pu, pv)] += self.ranks[max(pu, pv)]

        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m

        uf = UnionFindSet(len(arr))
        n, ans = len(arr), -1

        for step, a in enumerate(arr):
            a -= 1

            uf.ranks[a] = 1
            for j in (a - 1, a + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j] > 0:
                        uf.union(a, j)

        return ans
