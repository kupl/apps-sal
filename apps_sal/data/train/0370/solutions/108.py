from collections import defaultdict
from math import sqrt
class DSU(object):
    def __init__(self, n):
        self.ds = list(range(n))
    
    
    def find(self, v):
        if self.ds[v] != v:
            self.ds[v] = self.find(self.ds[v])
        return self.ds[v]

    def union(self, p1, p2):
        pp1, pp2 = self.find(p1), self.find(p2)
        self.ds[pp1] = pp2
    
class Solution(object):    
    def uniqPrime(self, n):
        l = []
        while n % 2 == 0:
            l.append(2)
            n = n//2
        
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                l.append(i)
                n = n//i
        if n > 2:
            l.append(n)
        
        return list(set(l))
        
    def largestComponentSize(self, A):
        primes = defaultdict(list)
        n = len(A)
        for i in range(n):
            p = self.uniqPrime(A[i])
            for x in p:
                primes[x].append(i)
        
        #now we need to merge the disjoint sets and see which is the longest
        uf = DSU(n)
        for i in primes.items():
            vals = i[1]
            for j in range(len(vals) - 1):
                uf.union(vals[j], vals[j+1])
        
        return max(Counter([uf.find(i) for i in range(n)]).values())
