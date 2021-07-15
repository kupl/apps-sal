import collections

class Union:
    
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.rank_count = collections.Counter()
        self.count = 0
        
    def add(self, pos):
        self.parent[pos] = pos
        self.rank[pos] = 1
        self.rank_count[1] += 1
        self.count += 1
    
    def find(self, pos): #recursively find parent
        if self.parent[pos] != pos:
            self.parent[pos] = self.find(self.parent[pos])
        return self.parent[pos]
    
    def unite(self, p, q):
        i, j = self.find(p), self.find(q)
        if i == j:
            return
        if self.rank[i] > self.rank[j]:
            i, j = j, i
        self.parent[i] = j # i is smaller tree, attach it to larger tree j with j as parent
        self.rank_count[self.rank[j]] -= 1
        self.rank_count[self.rank[i]] -= 1
        self.rank[j] += self.rank[i]
        self.rank_count[self.rank[j]] += 1
        self.count -= 1

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        bi = Union()
        for step, idx in enumerate(arr, 1):
            bi.add(idx)
            for neighbor in (idx + 1), (idx - 1):
                if neighbor in bi.parent:
                    bi.unite(idx, neighbor)
            if bi.rank_count.get(m, 0) > 0:  res = step
        return res

