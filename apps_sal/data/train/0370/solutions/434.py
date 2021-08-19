class UnionFind:

    def __init__(self, length):
        self.parents = {num: num for num in range(length)}
        self.ranks = {num: 1 for num in range(length)}

    def find(self, src):
        if self.parents[src] == src:
            return src
        self.parents[src] = self.find(self.parents[src])
        return self.parents[src]

    def union(self, src, dest):
        (rootSrc, rootDest) = (self.find(src), self.find(dest))
        if rootSrc == rootDest:
            return -1
        if self.ranks[rootSrc] > self.ranks[rootDest]:
            self.parents[rootDest] = rootSrc
            self.ranks[rootSrc] += self.ranks[rootDest]
            return self.ranks[rootSrc]
        else:
            self.parents[rootSrc] = rootDest
            self.ranks[rootDest] += self.ranks[rootSrc]
            return self.ranks[rootDest]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def genPrimes(num):
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return set([i]) | genPrimes(num // i)
                i += 1
            return set([num])
        uf = UnionFind(len(A))
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            primesNum = genPrimes(num)
            for prime in primesNum:
                primes[prime].append(i)
        for (_, indexes) in primes.items():
            for i in range(len(indexes) - 1):
                uf.union(indexes[i], indexes[i + 1])
        return max(uf.ranks.values())
