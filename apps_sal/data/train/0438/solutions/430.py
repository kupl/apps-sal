class DS:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return
        self.par[px] = py
        self.rank[py] += self.rank[px]
    
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ds = DS(len(arr))
        ans = -1
        b_arr = [0] * len(arr)
        
        for i, num in enumerate(arr):
            idx = num-1
            b_arr[idx] = 1
            
            if idx > 0 and b_arr[idx-1]:
                p = ds.find(idx-1)
                if ds.rank[p] == m:
                    ans = i
                ds.union(idx, idx-1)
                
            if idx < len(arr)-1 and b_arr[idx+1]:
                p = ds.find(idx+1)
                if ds.rank[p] == m:
                    ans = i
                ds.union(idx, idx+1)
                
            p = ds.find(idx)
            if ds.rank[p] == m:
                ans = i+1
        return ans
