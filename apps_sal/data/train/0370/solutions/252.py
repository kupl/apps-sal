class DSU:

    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        self.p[xr] = yr


class Solution:

    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set:
                primes[q].append(i)
        for (_, indexes) in list(primes.items()):
            for i in range(len(indexes) - 1):
                UF.union(indexes[i], indexes[i + 1])
        return max(Counter([UF.find(i) for i in range(n)]).values())


class UnionFind:

    def __init__(self, A):
        self.factorparent = []
        for i in range(A):
            self.factorparent.append(i)

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        self.factorparent[xp] = yp

    def find(self, x):
        if x != self.factorparent[x]:
            self.factorparent[x] = self.find(self.factorparent[x])
        return self.factorparent[x]


class Solution1:

    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        length = len(A)
        obj = UnionFind(length)
        primes = defaultdict(list)
        for (i, n) in enumerate(A):
            primeset = self.getPrime(n)
            for p in primeset:
                primes[p].append(i)
        for (k, v) in list(primes.items()):
            for i in range(len(v) - 1):
                obj.union(v[i], v[i + 1])
        primes = {}
        maxval = 0
        for i in range(length):
            val = obj.find(i)
            primes[val] = primes.get(val, 0) + 1
            maxval = max(maxval, primes[val])
        return maxval

    def getPrime(self, n):
        i = 2
        while i <= int(sqrt(n)):
            if n % i == 0:
                return self.getPrime(n // i) | set([i])
            i += 1
        return set([n])
