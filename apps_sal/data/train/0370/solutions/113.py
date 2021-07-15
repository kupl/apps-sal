class UnionFind(object):
    def uf(self, n):  
        self.uf = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):  
        while x != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return x

    def union(self, x, y):  
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0

def primeFactors(n):  # Prime factor decomposition
    out = set()
    while n % 2 == 0: 
        out.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i== 0: 
            out.add(i) 
            n //= i 
    if n > 2: 
        out.add(n)
    return out

class Solution(object):
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind()
        uf.uf(len(A))
        
        primeToIndex = {} 
        for i,a in enumerate(A):
            primes = primeFactors(a)
            for p in primes:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)
