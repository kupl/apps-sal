from collections import defaultdict


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        us = UnionSet(max(A))
        num_fac_map = dict()
        for num in A:
            primes = list(self.getPrimes(num))
            num_fac_map[num] = primes[0]
            for i in range(len(primes) - 1):
                us.union(primes[i], primes[i + 1])
        _max = 0
        most_linked_fac_map = defaultdict(int)
        for num in A:
            fac = us.find(num_fac_map[num])
            most_linked_fac_map[fac] += 1
            _max = max(_max, most_linked_fac_map[fac])
        return _max

    def getPrimes(self, num):
        primes = set()
        factor = 2
        while num >= factor * factor:
            if num % factor == 0:
                primes.add(factor)
                num //= factor
            else:
                factor += 1
        primes.add(num)
        return primes


class UnionSet:

    def __init__(self, size):
        self.factors = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, ix):
        while self.factors[ix] != ix:
            ix = self.factors[ix]
        return ix

    def union(self, ix1, ix2):
        (p1, p2) = (self.find(ix1), self.find(ix2))
        if p1 == p2:
            return
        if self.size[p1] > self.size[p2]:
            (p1, p2) = (p2, p1)
        self.factors[p1] = p2
        self.size[p2] += self.size[p1]
