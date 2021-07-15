class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu = DSU()
        ans = -1
        visited = set()
        previous_index = []
        for i, num in enumerate(arr):
            visited.add(num)
            if num - 1 in visited:
                dsu.union(num, num - 1)
            if num + 1 in visited:
                dsu.union(num, num + 1)
            
            current_index = [i for i in previous_index if dsu.getCount(i) == m]
            previous_index = current_index
            
            if dsu.getCount(num) == m:
                current_index.append(num)
            
            if previous_index:
                ans = i + 1
                
        return ans
            

class DSU:
    def __init__(self):
        self.father = {}
        self.count = {}
    
    def find(self, a):
        self.father.setdefault(a, a)
        self.count.setdefault(a, 1)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]
    
    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = _b
            self.count[_b] += self.count[_a]
    
    def getCount(self, a):
        return self.count[self.find(a)]
            

