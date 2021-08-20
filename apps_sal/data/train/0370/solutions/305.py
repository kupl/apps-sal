import math
from collections import defaultdict


class UF:

    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.sz = [1 for _ in range(n)]

    def find(self, x):
        while x != self.roots[x]:
            self.roots[x] = self.roots[self.roots[x]]
            x = self.roots[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.sz[root_x] >= self.sz[root_y]:
            self.roots[root_y] = root_x
            self.sz[root_x] += self.sz[root_y]
        else:
            self.roots[root_x] = root_y
            self.sz[root_y] += self.sz[root_x]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def factors(num):
            factor = 2
            prime_factors = []
            while num >= factor * factor:
                if num % factor == 0:
                    prime_factors.append(factor)
                    num = num // factor
                else:
                    factor += 1
            prime_factors.append(num)
            return prime_factors
        N = len(A)
        uf = UF(max(A) + 1)
        num_factor_map = defaultdict(int)
        for num in A:
            num_factors = factors(num)
            num_factor_map[num] = num_factors[0]
            for i in range(len(num_factors) - 1):
                uf.union(num_factors[i], num_factors[i + 1])
        counter = defaultdict(int)
        for num in A:
            counter[uf.find(num_factor_map[num])] += 1
        return max(counter.values())
