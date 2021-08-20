class UnionFind:

    def __init__(self, N):
        self.par = list(range(N))
        self.rank = [0] * N
        self.size = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        elif self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.size[px] += self.size[py]
        else:
            self.par[py] = px
            self.rank[px] += 1
            self.size[px] += self.size[py]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        N = max(A)
        primes = []
        res = 0
        for i in range(2, int(N ** 0.5) + 1):
            for j in primes:
                if i % j == 0:
                    break
            else:
                primes.append(i)
        uf = UnionFind(N + 1)
        used_primes = set()
        for a in A:
            if a < 2:
                continue
            a_primes = []
            for p in primes:
                if p * p > a:
                    break
                if a % p == 0:
                    a_primes.append(p)
                    while a % p == 0:
                        a //= p
            if a > 1:
                a_primes.append(a)
            idx = uf.find(a_primes[0])
            used_primes.add(a_primes[0])
            uf.size[idx] += 1
            for i in range(1, len(a_primes)):
                uf.union(a_primes[0], a_primes[i])
        for a in used_primes:
            idx = uf.find(a)
            res = max(res, uf.size[idx])
        return res
