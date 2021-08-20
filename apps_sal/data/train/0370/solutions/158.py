from math import sqrt
from collections import defaultdict, Counter


def get_prime_factors(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return {i} | get_prime_factors(n // i)
    return {n}


class Solution:

    def largestComponentSize(self, A):
        prime_multiples_map = defaultdict(list)
        for v in A:
            for factor in get_prime_factors(v):
                prime_multiples_map[factor].append(v)
        dsu = DSU(A)
        for vertices in list(prime_multiples_map.values()):
            last = vertices[0]
            for v in vertices:
                dsu.union(last, v)
        parents = [dsu.find(v) for v in A]
        counter = Counter(parents)
        return counter.most_common(1)[0][1]


class DSU:

    def __init__(self, nums):
        self.p = {n: n for n in nums}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px != py:
            self.p[px] = py
