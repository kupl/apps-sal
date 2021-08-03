class UF:
    def __init__(self, n):
        self.p = [i for i in range(n + 1)]
        self.counts = Counter()
        self.rank = [0 for i in range(n + 1)]

    def getParent(self, i):
        if self.p[i] == i:
            return i
        self.p[i] = self.getParent(self.p[i])
        return self.p[i]

    def set(self, i):
        self.counts[1] += 1
        self.rank[i] = 1

    def isSet(self, i):
        return 1 <= i < len(self.p) and self.rank[i] != 0

    def getCount(self, i):
        return self.counts[i]

    def connect(self, i, j):
        pi = self.getParent(i)
        pj = self.getParent(j)
        if pi != pj:
            self.p[pi] = pj
            ri, rj = self.rank[pi], self.rank[pj]
            self.counts[ri] -= 1
            self.counts[rj] -= 1
            self.counts[ri + rj] += 1
            self.rank[pj] = ri + rj


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UF(n)

        result = -1
        for i, e in enumerate(arr, start=1):
            uf.set(e)
            if uf.isSet(e - 1):
                uf.connect(e - 1, e)
            if uf.isSet(e + 1):
                uf.connect(e, e + 1)
            if uf.getCount(m) != 0:
                result = i

        return result
