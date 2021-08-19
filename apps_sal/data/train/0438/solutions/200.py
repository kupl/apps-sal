class UF:
    def __init__(self, e):
        self.parents = list(range(e))
        self.ranks = [0] * e

    def findP(self, r):
        if r == self.parents[r]:
            return r
        self.parents[r] = self.findP(self.parents[r])
        return self.parents[r]

    def union(self, u, v):
        up = self.findP(u)
        vp = self.findP(v)

        if up != vp:
            if self.ranks[up] >= self.ranks[vp]:
                self.parents[vp] = up

                self.ranks[up] += self.ranks[vp]
            else:
                self.parents[up] = vp
                self.ranks[vp] += self.ranks[up]
            return False
        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        if m == len(arr):
            return m

        n = len(arr)
        u = UF(n)

        res = -1

        for step, v in enumerate(arr):

            v = v - 1
            u.ranks[v] = 1

            for i in (v - 1, v + 1):
                if 0 <= i < n:
                    if u.ranks[u.findP(i)] == m:
                        res = step

                    if u.ranks[i]:
                        u.union(v, i)

            # print (step, u.ranks, u.parents)

            # if u.ranks[u.findP(v)]==m:
            #   res = step

        return res
