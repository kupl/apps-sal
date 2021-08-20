from math import sqrt
from collections import Counter


class UnionFind:

    def __init__(self, length):
        self.array = [i for i in range(length)]

    def union(self, x, y):
        xLoc = self.find(x)
        yLoc = self.find(y)
        self.array[xLoc] = yLoc

    def find(self, x):
        if x != self.array[x]:
            self.array[x] = self.find(self.array[x])
        return self.array[x]

    def most(self):
        for i in range(len(self.array)):
            self.find(i)
        count = Counter(self.array)
        return max(count.values())


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(len(A))

        def gcf(a, b):
            while b:
                (a, b) = (b, a % b)
            return a

        def primes(x):
            if x == 2:
                return {2}
            if x % 2 == 0:
                return primes(x // 2) | {2}
            for i in range(3, int(sqrt(x)) + 1, 2):
                if x % i == 0:
                    return primes(x // i) | {i}
            return {x}
        facts = {}
        for i in range(len(A)):
            for prime in primes(A[i]):
                if prime not in facts:
                    facts[prime] = []
                facts[prime].append(i)
        print(facts)
        for prime in facts:
            for i in range(len(facts[prime]) - 1):
                uf.union(facts[prime][i], facts[prime][i + 1])
        return uf.most()
