from collections import defaultdict, Counter


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
        xr, yr = list(map(self.find, (x, y)))
        if xr == yr:
            return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # Union-Find on Prime Factors
        # Time  complexity: O(N x (logM x logM + sqrt(M)))
        # Space complexity: O(M + N)
        # def primeDecompose(num):
        #     factor = 2
        #     prime_factors = []
        #     while num >= factor * factor:
        #         if num % factor == 0:
        #             prime_factors.append(factor)
        #             num //= factor
        #         else:
        #             factor += 1
        #     prime_factors.append(num)
        #     return prime_factors

        # dsu = DSU(max(A) + 1)
        # num_factor_map = {}

        # for num in A:
        #     prime_factors = list(set(primeDecompose(num)))
        #     # map a number to its first prime factor
        #     num_factor_map[num] = prime_factors[0]
        #     # merge all groups that contain the prime factors.
        #     for i in range(0, len(prime_factors) - 1):
        #         dsu.union(prime_factors[i], prime_factors[i + 1])

        # max_size = 0
        # group_count = defaultdict(int)
        # for num in A:
        #     group_id = dsu.find(num_factor_map[num])
        #     group_count[group_id] += 1
        #     max_size = max(max_size, group_count[group_id])

        # return max_size

        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x //= d
                    facs.append(d)
                d += 1
            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())
