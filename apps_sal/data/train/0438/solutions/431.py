class UnionFindSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pv == pu:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv
        else:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        ans = -1
        uf = UnionFindSet(n)
        for (step, i) in enumerate(arr):
            i -= 1
            uf.rank[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.rank[uf.find(j)] == m:
                        ans = step
                    print(uf.rank[uf.find(j)])
                    if uf.rank[j]:
                        uf.union(i, j)
        for i in range(n):
            if uf.rank[uf.find(i)] == m:
                return n
        return ans
