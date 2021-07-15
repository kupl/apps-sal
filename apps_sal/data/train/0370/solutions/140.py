        
class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
        
        
class Solution:
    def findPrime(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.findPrime(n//i) | set([i])
        return set([n])
    
    
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        uf = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pset = self.findPrime(num)
            for q in pset:
                primes[q].append(i)
        
        for _, indexes in list(primes.items()):
            for i in range(len(indexes) - 1):
                uf.union(indexes[i], indexes[i+1])
        return max(Counter([uf.find(i) for i in range(n)]).values())
        
        

        

