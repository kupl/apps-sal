class UF:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr != yr:
            if self.s[x] < self.s[y]:
                (xr, yr) = (yr, xr)
            self.p[yr] = xr
            self.s[xr] += self.s[yr]


class Solution:
    M = 100000
    sieve = [0] * (M + 1)
    for i in range(2, M + 1):
        if sieve[i] != 0:
            continue
        for j in range(1, M // i + 1):
            sieve[j * i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        g = UF(len(A))
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            while num > 1:
                q = self.sieve[num]
                primes[q].append(i)
                while num % q == 0:
                    num //= q
        for l in primes.values():
            x = l[0]
            for y in l[1:]:
                g.union(x, y)
        return max(g.s)
