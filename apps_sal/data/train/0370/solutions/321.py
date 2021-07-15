from collections import defaultdict, Counter
from functools import lru_cache

MAX_N = 100000


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # compute factors
        sieve = Sieve(MAX_N)
        factors = defaultdict(list)
        for x in A:
            for factor in sieve.factorize(x):
                factors[factor].append(x)
        '''
        f = Factors()
        factors = defaultdict(list)
        for x in A:
            for factor in f.find_for(x):
                factors[factor].append(x)
        '''

        uf = UnionFind()
        for values in list(factors.values()):
            for i in range(1, len(values)):
                uf.connect(values[i-1], values[i])
                
        return max(list(Counter(uf.root(x) for x in A).values()), default=0)
        '''
        
        # build bipartite graph from factors and values
        g = Graph()
        for factor, values in factors.items():
            g.add_factor(factor)
            for value in values:
                g.add_value(value)
                g.connect(factor, value)
        
        return g.find_largest_connected_size()
        '''

    
class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def connect(self, a, b):
        if a not in self.parents:
            self.parents[a] = a
        
        if b not in self.parents:
            self.parents[b] = b
            
        root = self.root(b)
        self.parents[self.root(a)] = root
        return root
    
    def root(self, a):
        if a not in self.parents:
            self.parents[a] = a
            return a

        if a == self.parents[a]:
            return a
        
        self.parents[a] = self.root(self.parents[a])
        
        return self.parents[a]


class Sieve:
    def __init__(self, max_n):
        self.primes = self._compute_primes(max_n)
        # better runtime than simply empty dict!
        self.factors = {p: [p] for p in self.primes}
        
    def _compute_primes(self, max_n):
        primes = list()
        sieve = [True] * (max_n+1)
        for prime in range(2, max_n+1):
            if not sieve[prime]:
                continue
            
            primes.append(prime)
            
            # better runtime than a manual while loop!
            for j in range(prime+prime, max_n+1, prime):
                sieve[j] = False
        
        return primes
    
    # this hurts the runtime!
    #@lru_cache(maxsize=MAX_N)
    def factorize(self, n):
        if n in self.factors:
            return self.factors[n]
        
        self.factors[n] = factors = set()
        work = n
        for prime in self.primes:
            # does not improve runtime!
            if work < prime:
                break
            
            if work % prime == 0:
                factors.add(prime)
                work //= prime
                
                factors.update(self.factorize(work))
                break

        return factors
        
        
class Graph:
    def __init__(self):
        self.adj = {}
        self.factors = set()
        self.values = set()
    
    def add_vertex(self, p, label):
        if p not in self.adj:
            self.adj[p] = set()
        if label == 'factor':
            self.factors.add(p)
        else:
            self.values.add(p)
    
    def add_factor(self, factor):
        self.add_vertex(factor, 'factor')
        
    def add_value(self, value):
        self.add_vertex(value, 'value')
        
    def connect(self, p, q):
        self.adj[p].add(q)
        self.adj[q].add(p)

    def find_largest_connected_size(self):
        seen = set()
        largest = 0
        for p in list(self.adj.keys()):
            count = self._dfs_from(p, seen)
            largest = max(largest, count)
            
        return largest
    
    def _dfs_from(self, p, seen):
        if p in seen:
            return 0
        
        seen.add(p)
        
        count = 1 if p in self.values else 0
        
        return count + sum(self._dfs_from(q, seen) for q in self.adj[p])

