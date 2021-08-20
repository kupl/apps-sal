from collections import defaultdict


class DSU:

    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
        self.siz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (xr, yr) = list(map(self.find, (x, y)))
        if xr == yr:
            return
        if self.rnk[xr] < self.rnk[yr]:
            (xr, yr) = (yr, xr)
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def primeDecompose(num):
            factor = 2
            prime_factors = []
            while num >= factor * factor:
                if num % factor == 0:
                    prime_factors.append(factor)
                    num //= factor
                else:
                    factor += 1
            prime_factors.append(num)
            return prime_factors
        dsu = DSU(max(A) + 1)
        num_factor_map = {}
        for num in A:
            prime_factors = list(set(primeDecompose(num)))
            num_factor_map[num] = prime_factors[0]
            for i in range(0, len(prime_factors) - 1):
                dsu.union(prime_factors[i], prime_factors[i + 1])
        max_size = 0
        group_count = defaultdict(int)
        for num in A:
            group_id = dsu.find(num_factor_map[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])
        return max_size
