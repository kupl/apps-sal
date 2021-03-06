class DSU:

    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        self.p[xr] = yr


class Solution:

    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            q = 2
            while q * q <= num:
                if num % q == 0:
                    primes[q].append(i)
                    while num % q == 0:
                        num = num // q
                q += 1
            if num > 1:
                primes[num].append(i)
        for (_, indexes) in primes.items():
            for i in range(len(indexes) - 1):
                UF.union(indexes[i], indexes[i + 1])
        return max(Counter([UF.find(i) for i in range(n)]).values())
