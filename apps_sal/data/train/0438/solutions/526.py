class UnionFind:
    def __init__(self, n):
        self.leaders = {}
        self.ranks = {}
        self.size = {}
        
    def add(self, x):
        if x in self.leaders:
            return
        self.leaders[x] = x
        self.ranks[x] = 1
        self.size[x] = 1
    
    def find(self, x):
        # p = x
        # while p != self._leaders[p]:
        #     p = self._leaders[p]
        # while x != p:
        #     self._leaders[x], x = p, self._leaders[x]
        # return p
        if self.leaders[x] != x:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]
    
    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q: 
            return False
        if self.ranks[p] < self.ranks[q]:
            self.leaders[p] = q
            self.size[q] += self.size[p]
        elif self.ranks[p] > self.ranks[q]:
            self.leaders[q] = p
            self.size[p] += self.size[q]
        else:        
            self.leaders[q] = p
            self.ranks[p] += 1
            self.size[p] += self.size[q]
        return True
    
class Solution:
    def findLatestStep(self, arr, m):
        n = len(arr)
        if n == m:
            return m
        uf = UnionFind(n)
        state = 0
        res = -1
        for i, x in enumerate(arr):
            uf.add(x)
            state ^= (1 << x)
            if x - 1 >= 1 and state & (1 << (x - 1)) != 0:
                if uf.size[uf.find(x - 1)] == m:
                    res = i
                uf.union(x, x - 1)
            if x + 1 <= n and state & (1 << (x + 1)) != 0:
                if uf.size[uf.find(x + 1)] == m:
                    res = i
                uf.union(x, x + 1)
        return res
