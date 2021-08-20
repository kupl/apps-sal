class DFU:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        self.p[xr] = yr


class Solution:

    def prime_sets(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.prime_sets(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        UF = DFU(len(A))
        primes = collections.defaultdict(list)
        for (i, n) in enumerate(A):
            prime_set = self.prime_sets(n)
            for q in prime_set:
                primes[q].append(i)
        for (_, items) in primes.items():
            for i in range(len(items) - 1):
                UF.union(items[i], items[i + 1])
        return max(Counter([UF.find(i) for i in range(len(A))]).values())
