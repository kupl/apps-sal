class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # [3,1,5,4,2]
        uf = UF(len(arr) + 1)
        res, step = -1, 1
        ok = set()
        for i in arr:
            uf.isOne[i] = True
            if i - 1 > 0 and uf.isOne[i - 1]:
                uf.union(i - 1, i)
            if i + 1 <= len(arr) and uf.isOne[i + 1]:
                uf.union(i, i + 1)
            curok = set()
            curf = uf.find(i)
            curones = uf.rank[curf]
            if curones == m:
                curok.add(curf)

            for f in ok:
                newf = uf.find(f)
                if uf.rank[newf] == m:
                    curok.add(newf)
            ok = curok
            if len(ok) > 0:
                res = step
            step += 1
        return res


class UF:
    def __init__(self, n):
        self.n = n
        self.fathers = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.isOne = [False for _ in range(n)]

    def find(self, x):
        if x != self.fathers[x]:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            count = self.rank[fx] + self.rank[fy]
            if self.rank[fx] > self.rank[fy]:
                self.fathers[fx] = fy
                self.rank[fy] = count
            else:
                self.fathers[fy] = fx
                self.rank[fx] = count
