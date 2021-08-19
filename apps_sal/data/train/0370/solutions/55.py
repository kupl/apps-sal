class UF:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    sieve = [0] * 100001
    for i in range(2, 100001):
        if sieve[i] != 0:
            continue
        for j in range(1, 100000 // i + 1):
            sieve[j * i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        g = UF(n)
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            while num > 1:
                q = self.sieve[num]
                primes[q].append(i)
                while num % q == 0:
                    num //= q
        for l in primes.values():
            (j, r) = (l[0], g.find(l[0]))
            for i in l[1:]:
                nd = g.find(i)
                if nd != r:
                    g.p[nd] = r
                    g.s[r] += g.s[nd]
        return max(g.s)
