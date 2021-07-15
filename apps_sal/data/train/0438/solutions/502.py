class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        self.m = m
        n = len(arr)
        self.parents = [i for i in range(n + 1)]
        self.grpcounts = {}
        self.countMgrps = 0
        
        last = -1
        for step, pos in enumerate(arr):
            self.grpcounts[pos] = 1
            if m == 1:
                self.countMgrps += 1
            
            if pos + 1 <= n and self.find(pos + 1) in self.grpcounts:
                self.union(pos, pos + 1)
            if pos - 1 > 0 and self.find(pos - 1) in self.grpcounts:
                self.union(pos, pos - 1)
            
            # print(self.countMgrps)
            if self.countMgrps > 0:
                last = step + 1
        
        return last
        
        
    def find(self, pos):
        path = []
        while pos != self.parents[pos]:
            path.append(pos)
            pos = self.parents[pos]
        
        for p in path:
            self.parents[p] = pos
        
        return pos
    
    
    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if p1 != p2:
            self.parents[p1] = p2
            if self.grpcounts[p1] == self.m:
                self.countMgrps -= 1
            if self.grpcounts[p2] == self.m:
                self.countMgrps -= 1
            
            self.grpcounts[p2] += self.grpcounts[p1]
            if self.grpcounts[p2] == self.m:
                self.countMgrps += 1
            
            del self.grpcounts[p1]

