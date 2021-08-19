class DSU:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (x1, y2) = (self.find(x), self.find(y))
        self.p[x1] = y2


class Solution:

    def primes(self, n):
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                return set([i]).union(self.primes(n // i))
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        prime = defaultdict(list)
        for (i, n) in enumerate(A):
            primeset = self.primes(n)
            for p in primeset:
                prime[p].append(i)
        N = len(A)
        dsu = DSU(N)
        for (_, indexes) in list(prime.items()):
            for i in range(len(indexes) - 1):
                dsu.union(indexes[i], indexes[i + 1])
        return max(Counter([dsu.find(i) for i in range(N)]).values())
