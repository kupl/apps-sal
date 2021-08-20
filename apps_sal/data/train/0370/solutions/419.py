class UnionFind:

    def __init__(self, val):
        self.val = val
        self.parent = self

    def union(self, uf):
        uf.find().parent = self.find()

    def find(self):
        while self.parent is not self.parent.parent:
            self.parent = self.parent.parent
        return self.parent


class Solution:

    def primeSet(self, n, cache):
        if n in cache:
            return cache[n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                cache[n] = self.primeSet(n // i, cache) | set([i])
                return cache[n]
        cache[n] = set([n])
        return cache[n]

    def largestComponentSize(self, A: List[int]) -> int:
        unionFinds = {x: UnionFind(x) for x in A}
        cache = {}
        primeToNumberMap = defaultdict(list)
        for x in A:
            primes = self.primeSet(x, cache)
            for p in primes:
                primeToNumberMap[p].append(x)
        for p in primeToNumberMap:
            for i in range(len(primeToNumberMap[p]) - 1):
                unionFinds[primeToNumberMap[p][i]].union(unionFinds[primeToNumberMap[p][i + 1]])
        return max(Counter([unionFinds[x].find().val for x in A]).values())
