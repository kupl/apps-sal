import math

class DiscreteSet:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
    
    def findP(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findP(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xp, yp = self.findP(x), self.findP(y)
        self.parent[xp] = yp

class Solution:
    def primesSet(self, n):
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return self.primesSet(n//i) | set([i])
        return set([n])
    
    def largestComponentSize(self, A: List[int]) -> int:
        dset = DiscreteSet(len(A))
        primes = defaultdict(list)
        
        for i, num in enumerate(A):
            prSet = self.primesSet(num)
            print((i,num,prSet))
            for pr in prSet: primes[pr].append(i)
        
        for indices in list(primes.values()):
            for i in range(len(indices)-1):
                dset.union(indices[i], indices[i+1])

        cnt = Counter()
        for i in range(len(A)):
            cnt[dset.findP(i)] += 1
        return max(cnt.values())

