class DFU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr


class Solution:
    def primes_set(self, d):
        for i in range(2, int(math.sqrt(d)) + 1):
            if d % i == 0:
                return self.primes_set(d // i) | set([i])
        return set([d])

    def largestComponentSize(self, A: List[int]) -> int:
        UF = DFU(len(A))
        primes = collections.defaultdict(list)

        for i, d in enumerate(A):
            primes_set = self.primes_set(d)
            for q in primes_set:
                primes[q].append(i)

        for key, items in list(primes.items()):
            for i in range(len(items) - 1):
                UF.union(items[i], items[i + 1])

        return max(Counter([UF.find(i) for i in range(len(A))]).values())
