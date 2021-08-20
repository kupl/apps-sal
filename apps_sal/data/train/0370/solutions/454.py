class DSU:

    def __init__(self, vals):
        self.p = {v: v for v in vals}

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union(self, u, v):
        (pu, pv) = (self.find(u), self.find(v))
        if pu != pv:
            self.p[pu] = pv


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        factors = collections.defaultdict(list)
        primes = self.getPrimes(int(math.sqrt(max(A))))
        for a in A:
            x = a
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors[a].append(x)
                primes.append(x)
        primes = list(set(primes))
        dsu = DSU(primes)
        for a in A:
            if a == 1:
                continue
            p0 = factors[a][0]
            for p in factors[a][1:]:
                dsu.union(p0, p)
        cnt = collections.Counter((dsu.find(factors[a][0]) for a in A if a > 1))
        return max(cnt.values())

    def getPrimes(self, v):
        primes = []
        for x in range(2, v + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)
        return primes
