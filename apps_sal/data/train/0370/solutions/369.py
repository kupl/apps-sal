class Solution:
    
    def _factorize(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self._factorize(n//i) | set([i])
        return set([n])
    
    def largestComponentSize(self, A: List[int]) -> int:
        primes = set()
        factors = {}
        for x in A:
            f = self._factorize(x)
            primes |= f
            factors[x] = list(f)
        
        uf = UF(primes, A)
        for x in A:
            for j in range(len(factors[x])):
                uf.union(x, factors[x][j])
            uf.sz[uf.root(x)] += 1
        
        return max([v for _, v in uf.sz.items()])


class UF:
    def __init__(self, primes, A):
        self.parent = {p: p for p in primes}
        for p in A:
            self.parent[p] = p
        self.sz = {p: 0 for p in primes}
        for p in A:
            self.sz[p] = 0
    
    def root(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        r_u = self.root(u)
        r_v = self.root(v)
        if r_u == r_v:
            return
        
        if self.sz[r_u] > self.sz[r_v]:
            self.parent[r_v] = r_u
            self.sz[r_u] += self.sz[r_v]
        else:
            self.parent[r_u] = r_v
            self.sz[r_v] += self.sz[r_u]
