class UF:
    def __init__(self, n):
        self.f = list(range(n))
        self.cc = [1] * n
        
    def find(self, x):
        while x != self.f[x]: # while, not if
            x = self.f[x]
        return x

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy: #
            if self.cc[fx] <= self.cc[fy]: # path compression?
                self.f[fx] = fy
                self.cc[fx], self.cc[fy] = 0, self.cc[fx] + self.cc[fy]
            else:
                self.f[fy] = fx
                self.cc[fy], self.cc[fx] = 0, self.cc[fx] + self.cc[fy]
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        uf = UF(n)
        
        '''
        # TLE
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if gcd(A[i], A[j]) > 1:
                    uf.union(i, j)
        '''
        
        def getPrimeSets(num, num2primes):
            if num2primes[num]:
                return num2primes[num]
            
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    num2primes[num] = getPrimeSets(i, num2primes) | getPrimeSets(num // i, num2primes)
                    return num2primes[num]
                
            num2primes[num] = set([num]) # num is prime
            return num2primes[num]
            
        num2primes = collections.defaultdict(set)
        for num in sorted(A):
            getPrimeSets(num, num2primes)
        
        prime2numIdxs = collections.defaultdict(list)
        for idx, num in enumerate(A):
            ps = num2primes[num]
            for p in ps:
                prime2numIdxs[p].append(idx)
                
        for _, idxs in list(prime2numIdxs.items()):
            for i in range(len(idxs) - 1):
                uf.union(idxs[i], idxs[i+1])
            
        # print(uf.f)
        # print(uf.cc)
        res = 1
        for i in range(n):
            res = max(uf.cc[i], res)
        return res

