class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, a, b):
        aPar = self.find(a)
        bPar = self.find(b)
        if aPar == bPar:
            return
        if self.size[aPar] > self.size[bPar]:
            self.parents[bPar] = aPar
            self.size[aPar] += self.size[bPar]
        else:
            self.parents[aPar] = bPar
            self.size[bPar] += self.size[aPar]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        uf = UnionFind(N)
        isAlive = [False] * N
        numM = 0
        latest = -1
        for (index, i) in enumerate(arr):
            isAlive[i - 1] = True
            if i != 1 and isAlive[i - 2]:
                if uf.size[uf.find(i - 2)] == m:
                    numM -= 1
                uf.union(i - 1, i - 2)
            if i != N and isAlive[i]:
                if uf.size[uf.find(i)] == m:
                    numM -= 1
                uf.union(i - 1, i)
            if uf.size[uf.find(i - 1)] == m:
                numM += 1
            if numM > 0:
                latest = index + 1
        return latest
