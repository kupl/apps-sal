class UnionFind:
    def __init__(self, count):
        self._parent = list(range(count))
        self._size = [1] * count
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]
    
    def find(self, x):
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        
        return self._parent[x]
    
    def size(self, x):
        return self._size[self.find(x)]
            

def prime_factors(num):
    if num < 2:
        return []
    
    factors = []
    
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            factors.append(factor)
            while num % factor == 0:
                num //= factor
            if num == 1:
                break
    
    if num > 1:
        factors.append(num)
    
    return factors


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        
        length = len(A)
        union_find = UnionFind(length)
        roots = {}
        
        for index, num in enumerate(A):
            for factor in prime_factors(num):
                if factor not in roots:
                    roots[factor] = index
                union_find.union(roots[factor], index)
        
        return max(union_find.size(index) for index in range(length))

