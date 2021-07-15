class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        table = collections.defaultdict(int)
        size = [0] * len(arr)
        parent = [-1] * len(arr)
        res = 0
        for i in range(len(arr)):
            pos = arr[i] - 1
            idx = self.find(pos, parent)
            if idx == -1:
                parent[pos] = pos
                size[pos] = 1
                table[size[pos]] = table[size[pos]] + 1
            self.unionAround(pos, arr, parent, size, table)
            if m in table:
                res = i + 1
        if res == 0:
            return -1
        return res
        
    
    def unionAround(self, i, arr, parent, size, table):
        if i > 0:
            self.union(i, i-1, parent, size, table)
        if i < len(arr) - 1:
            self.union(i, i+1, parent, size, table)
    
    def union(self, i, j, parent, size, table):
        x = self.find(i, parent)
        y = self.find(j, parent)
        if y == -1:
            return
        if x != y:
            table[size[y]] = table[size[y]]-1
            if table[size[y]] == 0:
                del table[size[y]]
                
            table[size[x]] = table[size[x]]-1
            if table[size[x]] == 0:
                del table[size[x]]
            
            size[y] += size[x]
            parent[x] = y
            
            table[size[y]] = table[size[y]] + 1
    
    def find(self, i, parent):
        if parent[i] == -1:
            return -1
        if parent[i] == i:
            return i
        return self.find(parent[i], parent)
        
        
        
        
        
        

