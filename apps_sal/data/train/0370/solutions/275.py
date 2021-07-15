from math import sqrt

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if self.find(x) == self.find(y): return
        
        xrank = self.rank[x]
        yrank = self.rank[y]
        
        if xrank < yrank:
            self.parent[self.find(x)] = self.find(y)
            self.rank[x] = self.rank[y] + 1
        else: 
            self.parent[self.find(y)] = self.find(x)
            self.rank[y] = self.rank[x] + 1
        
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        
        uf = DSU(n)
        
        def fac(x):
            yield x
            for i in range(2, int(sqrt(x))+1): 
                if x % i == 0: 
                    yield i
                    yield x // i
                                
        graph = {}
        
        for idx, x in enumerate(A):   
            for e in fac(x):
                if e in graph: uf.union(idx, graph[e])
                graph[e] = idx
        
        ctr = collections.Counter()
        for i in range(n):
            ctr[uf.find(i)] += 1
        
        return ctr.most_common()[0][1]

