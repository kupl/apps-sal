from math import sqrt
from collections import defaultdict
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        union = DisjoinSet(max(A))
        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    union.union(a, factor)
                    union.union(a, a // factor)
        result = 0
        counter = defaultdict(int)
        for i in A:
            parent = union.find(i)
            counter[parent] += 1
            result = max(result, counter[parent])
        return result
    
class DisjoinSet:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1 for _ in range(size + 1)]
        
    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def union(self, i, j):
        parentI, parentJ = self.find(i), self.find(j)
        if parentI == parentJ:
            return
        if self.size[parentI] >= self.size[parentJ]:
            big, small = parentI,parentJ
        else:
            big, small = parentJ, parentI
        self.size[big] += self.size[small]
        self.parent[small] = big

