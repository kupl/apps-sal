class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] > self.size[pv]:
            (pu, pv) = (pv, pu)
        self.parent[pu] = pv
        self.size[pv] += self.size[pu]
        return True


class Solution:

    def sharecommon(self, a, b):
        for k in range(2, min(a, b) + 1):
            if a % k == 0 and b % k == 0:
                return True
        return False

    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        ufs = UnionFind(max(A))
        foundSet = collections.defaultdict(int)
        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    ufs.union(a, factor)
                    ufs.union(a, a // factor)
        for a in A:
            foundSet[ufs.find(a)] += 1
        return max(foundSet.values()) if foundSet else 1
