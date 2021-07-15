class UnionFind(object):
    def uf(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):  
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.root[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def primeFactors(n):
            primes = set()
            while n % 2 == 0:
                primes.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)+1), 2):
                while n % i == 0:
                    primes.add(i)
                    n //= i
            if n > 2: #incase 3
                primes.add(n)
            return primes
        uf = UnionFind()
        uf.uf(len(A))
        pF = {}
        for i, num in enumerate(A):
            primes = primeFactors(num)
            for p in primes:
                if p in pF:
                    uf.union(i, pF[p])
                pF[p] = i
        return max(uf.size)
