# Reference: https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/819772/TLE-Python-GCD-%2B-Union-Find-%2B-Rank-Compression

from typing import List
from math import gcd, sqrt
from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.sizes = [1] * size
        self.parent = [i for i in range(size)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.sizes[root_u] < self.sizes[root_v]:
                self.parent[root_u] = root_v
                self.sizes[root_v] += self.sizes[root_u]
            else:
                self.parent[root_v] = root_u
                self.sizes[root_u] += self.sizes[root_v]

    def size(self, u):
        return self.sizes[self.find(u)]

from itertools import count
def primes():
    def _not_divisible(n):
        return lambda x: x % n > 0
    yield 2
    odd = count(3, 2)
    while True:
        n = next(odd)
        yield n
        # sieve of Eratosthenes
        odd = list(filter(_not_divisible(n), odd))

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # O(n * sqrt(max(A)))
        dsu = DSU(max(A) + 1)   # 0 is not being used

        for x in A:
            for factor in range(2, int(sqrt(x)) + 1):
                if x % factor == 0:
                    dsu.union(x, factor)
                    dsu.union(x, x // factor)

        ans, counter = 0, defaultdict(int)
        for x in A:
            counter[dsu.find(x)] += 1
            ans = max(ans, counter[dsu.find(x)])
        return ans

        # # O(n^2)
        # dsu = DSU(len(A))
        # for i in range(len(A)):
        #     for j in range(len(A)):
        #         if i != j and gcd(A[i], A[j]) > 1:
        #             dsu.union(i, j)
        # return max(dsu.sizes)

