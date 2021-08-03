class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.sz = [1] * N
        self.max_sz = 1

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.sz[xr] < self.sz[yr]:
            x, y, xr, yr = y, x, yr, xr
        self.p[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.max_sz = max(self.max_sz, self.sz[xr])


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0

        primes = []
        for x in range(2, int(max(A)**0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)

        def factors(x):
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    yield p
                    while x % p == 0:
                        x //= p
            if x > 1:
                primes.append(x)
                yield x

        dsu = DSU(len(A))
        div_idx = dict()
        for i, a in enumerate(A):
            for p in factors(a):
                div_idx.setdefault(p, []).append(i)

        for indices in div_idx.values():
            for i in range(len(indices) - 1):
                dsu.union(indices[i], indices[i + 1])
        return dsu.max_sz
