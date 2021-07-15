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
    def primes_set(self, d):
        for i in range(2, int(math.sqrt(d)) + 1):
            if d % i == 0:
                return self.primes_set(d // i) | set([i])
        return set([d])
    
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)
            
        for _, indexes in primes.items():
            for i in range(len(indexes) - 1):
                UF.union(indexes[i], indexes[i + 1])
        
        return max(Counter([UF.find(i) for i in range(n)]).values())
