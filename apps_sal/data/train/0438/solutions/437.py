class UnionFind(object):
    def __init__(self):
        self.parents = dict()
        self.sizes = dict()
    
    def __contains__(self, i):
        return self.parents.__contains__(i)
    
    def insert(self, i):
        self.parents[i] = i
        self.sizes[i] = 1

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  
            i = self.parents[i]
        return i

    def union(self, p, q):
        root_p, root_q = list(map(self.find, (p, q)))
        if root_p == root_q: return
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]    


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UnionFind()
        step_wanted = -1
        n = len(arr)
        for step, pos in enumerate(arr, 1):
            uf.insert(pos)
            for neighbor in [pos-1, pos+1]:
                if neighbor not in uf: continue
                if uf.sizes[uf.find(neighbor)] == m: step_wanted = step - 1
                uf.union(pos, neighbor)
        for i in range(1, n+1):
            if uf.sizes[uf.find(i)] == m:
                step_wanted = n
        return step_wanted

