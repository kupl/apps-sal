from math import sqrt
from collections import Counter


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        self.parent[root2] = root1


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)

        ds = DisjointSet(n)

        def prime_set(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return prime_set(n // i) | set([i])

            return set([n])

        primes = {}
        for i in range(n):
            for prime in prime_set(A[i]):
                primes[prime] = primes.get(prime, []) + [i]

        for _, indices in list(primes.items()):
            for i in range(len(indices) - 1):
                ds.union(indices[i], indices[i + 1])

        print((ds.parent))
        print(primes)

        return max(Counter([ds.find(i) for i in range(n)]).values())
