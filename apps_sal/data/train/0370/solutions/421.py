class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        self.Max = 1
    
    def find(self, e):
        if self.parent[e] != e:
            self.parent[e] = self.find(self.parent[e])
        return self.parent[e]
    
    def union(self, x, y):
        headx = self.find(x)
        heady = self.find(y)
        if headx != heady:
            self.parent[headx] = heady
            self.size[heady] += self.size[headx]
            self.Max = max(self.Max, self.size[heady])


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # helper to get a list prime factors of a given integer
        def primeFact(num):
            res = []
            n = num
            if n % 2 == 0:
                res.append(2)
                n /= 2
            while n % 2 == 0:
                n /= 2
            f = 3
            lim = int(sqrt(n) + 1)
            while f < lim and n > 1:
                if n % f == 0:
                    res.append(f)
                    n /= f
                while n % f == 0:
                    n /= f
                f += 2
            if n > 2:
                res.append(int(n))
            return res
        
        # use a dictionary to store all indexes of each factor
        uf = UnionFind(len(A))
        d = {}
        for i, num in enumerate(A):
            factors = primeFact(num)
            for factor in factors:
                if factor not in d:
                    d[factor] = [i]
                else:
                    d[factor].append(i)
                    
        # compute unions
        for factor in d:
            for j in range(len(d[factor]) - 1):
                uf.union(d[factor][j], d[factor][j+1])
        # return size of largest union
        return uf.Max

