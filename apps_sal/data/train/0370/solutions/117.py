'''
Idea: 1. Prime factorize the given numbers
      2. Map the factors to the indices in which they take part
      3. Perform union operations on the list of indices belonging to same factor
      4. Perform union operation to find the largest component

Time complexity: O(n * sqrt(m)) where prime factorization 'sqrt(m)' is applied n times 
Space complexity: O(n * log(m)) to keep all prime factors and maintain DSU
'''

import collections, math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sizeOf = [1] * n  
    

    def find(self, p):
        # Find parent of given node
        root = p
        while self.parent[root] != root:
            root = self.parent[root]

        # Path compression
        while p != root:
            next_node = self.parent[root]    
            self.parent[p] = root
            p = next_node
        
        return root 

    
    def union(self, x, y):
        r1, r2 = self.find(x), self.find(y)

        if r1 == r2:
            return 
        if self.sizeOf[r1] > self.sizeOf[r2]:
            self.sizeOf[r1] += self.sizeOf[r2]
            self.parent[r2] = r1 
        else:
            self.sizeOf[r2] += self.sizeOf[r1]
            self.parent[r1] = r2


class Solution:
    def largestComponentSize(self, A):

        def primeFactorization(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return primeFactorization(n//i) | set([i]) 
            return set([n])


        n = len(A)
        dsu = DSU(n)
        primes = collections.defaultdict(list)

        for i in range(n):
            prime_factors = primeFactorization(A[i])
            for factor in prime_factors:
                primes[factor] += i, 
        
        for factor in primes:
            indices = primes[factor]
            size = len(indices)
            for i in range(size-1):
                dsu.union(indices[i], indices[i+1]) 
        
        components = collections.defaultdict(int)
        
        for index in range(n):
            components[dsu.find(index)] += 1
        
        return max(components.values())

        

