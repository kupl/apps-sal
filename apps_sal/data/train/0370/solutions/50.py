class UF(object):
    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while x != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return x

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        self.uf[xr] = yr
        self.size[yr] += self.size[xr]
        self.size[xr] = 0


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def pf(n):
            F = set()
            if n % 2 == 0:
                F.add(2)
                while n % 2 == 0:
                    n //= 2
            for f in range(3, int(n**0.5) + 1, 2):
                if n % f == 0:
                    F.add(f)
                    while n % f == 0:
                        n //= f
            if n > 1:
                F.add(n)
            return F

        uf = UF(len(A))

        pd = {}
        for i, a in enumerate(A):
            F = pf(a)
            print((a, F))
            for p in F:
                if p in pd:
                    uf.union(i, pd[p])
                pd[p] = i

        return max(uf.size)
