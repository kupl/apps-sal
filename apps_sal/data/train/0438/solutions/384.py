class UnionSet:
    def __init__(self, n):
        self.par = list(range(n))
        self.ed = list(range(n))

    def find(self, i):
        if self.par[i] != i:
            par = self.find(self.par[i])
            self.par[i] = par
        return self.par[i]

    def merge(self, i, j):
        par1 = self.find(i)
        par2 = self.find(j)
        ed1 = self.ed[par1]
        ed2 = self.ed[par2]
        self.par[max(par1, par2)] = min(par1, par2)
        self.ed[par1] = self.ed[par2] = max(ed1, ed2)

    def get_ed(self, i):
        return self.ed[i]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        us = UnionSet(n)
        bits = [0] * n
        result = -1
        cnt = 0
        for i, pos in enumerate(arr):
            pos -= 1
            bits[pos] = 1
            if pos > 0 and bits[pos - 1] == 1:
                st = us.find(pos - 1)
                ed = us.get_ed(st)
                if ed - st + 1 == m:
                    cnt -= 1
                us.merge(pos, pos - 1)
            if pos < n - 1 and bits[pos + 1] == 1:
                st = us.find(pos + 1)
                ed = us.get_ed(st)
                if ed - st + 1 == m:
                    cnt -= 1
                us.merge(pos, pos + 1)
            st = us.find(pos)
            ed = us.get_ed(st)
            if ed - st + 1 == m:
                cnt += 1
            if cnt > 0:
                result = i + 1
        return result
