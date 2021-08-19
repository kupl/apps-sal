import collections
import math


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        #self.size = [1] * n

    def find(self, x):
        # print(x)
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
        # return x if self.par[x] == x else self.par[x] = self.find(self.par[x])

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.par[xr] = yr
        #self.size[yr] += self.size[xr]
        #self.size[xr] = 0


class Solution:
    def sieve(self, n):  # best sieve i have ever seen
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.sieve(n // i) | set([i])
        # print(n) #this is def for 2,3
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        dsu = DSU(n)
        primes_and_multiples = collections.defaultdict(list)
        for i, num in enumerate(A):
            factors = self.sieve(num)
            for factor in factors:
                primes_and_multiples[factor].append(i)
        for primes in list(primes_and_multiples.values()):
            for i in range(len(primes) - 1):  # could have done i-1, i with 1,len(primes)
                dsu.union(primes[i], primes[i + 1])
        # return max(dsu.size)
        return max(collections.Counter([dsu.find(i) for i in range(n)]).values())
