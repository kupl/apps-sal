class DS:
    def __init__(self, n):
        self.par = list(range(n))
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        @lru_cache(None)
        def find_prime_factors(num):
            if num == 1:
                return []
            
            if num <= 3:
                return [num]
            
            for prime in range(2, int(sqrt(num))+1):
                if num % prime == 0:
                    break
            else:
                prime = num
                    
            while num % prime == 0:
                num //= prime
            return [prime] + find_prime_factors(num)
        
        s = {}
        for i,num in enumerate(A):
            if num == 1:
                continue
            primes = find_prime_factors(num)
            for prime in primes:
                if prime not in s:
                    s[prime] = []
                s[prime] += [i]

        ds = DS(len(A))
        for prime in s:
            for i in range(len(s[prime])-1):
                ds.union(s[prime][i], s[prime][i+1])
            
        counter = Counter([ds.find(i) for i in range(len(A))])
        return max(counter.values() or [1])
