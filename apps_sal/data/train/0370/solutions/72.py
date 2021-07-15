class Solution:
    def primeFactors(self, n):
        pset = set()
        # While n is even, divide by two
        while n % 2 == 0:
            pset.add(2)
            n = n // 2
        
        # For every odd i between 3 and sqrt(n), check if it's a factor
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                pset.add(i)
                n = n // i
        
        # If n is still greater than 2, it's a prime
        if n > 2:
            pset.add(n)
            
        return pset
    
    def largestComponentSize(self, A: List[int]) -> int:
        # Creates a disjoint set (union find) for the list A
        ds = DisjointSet(A)
        
        # Dict to keep the index of the disjoint set root for every prime divisor set found
        primeRoots = {}
        
        # Iterate over A and find it's prime divisors
        for i, a in enumerate(A):
            primes = self.primeFactors(a)
            # For every prime, set the index of a as it's root
            for p in primes:
                # If already have a set for this prime, join the current element to it
                if p in primeRoots:
                    ds.union(i, primeRoots[p])
                else:
                    primeRoots[p] = i

        return max(ds.sizes)
    

class DisjointSet:
    def __init__(self, elements):
        self.parents = [x for x in range(len(elements))]
        self.sizes = [1] * len(elements)
        
    # Path splitting find algorithm.
    def find(self, x):
        while x != self.parents[x]:
                x, self.parents[x] = self.parents[x], self.parents[self.parents[x]]
        return x
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return px
        
        if self.sizes[px] > self.sizes[py]:
            py, px = px, py
            
        self.parents[px] = py
        self.sizes[py] += self.sizes[px]
