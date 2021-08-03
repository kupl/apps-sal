class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.s[xr] += self.s[yr]
        self.p[yr] = xr


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def add_prime(i, j, primes):
            if i not in primes:
                primes[i] = [j]
            else:
                primes[i].append(j)

        g = UF(len(A))
        primes = {}
        for j, k in enumerate(A):
            i = 2
            while i * i <= k:
                if k % i == 0:
                    add_prime(i, j, primes)
                    while k % i == 0:
                        k = k // i
                i += 1
            if k > 1:
                add_prime(k, j, primes)
        # print(primes)
        for l in primes.values():
            j, r = l[0], g.find(l[0])
            for i in l[1:]:
                if g.find(i) != r:
                    g.union(j, i)
        # print(g.p)
        # print(g.s)
        return max(g.s)
