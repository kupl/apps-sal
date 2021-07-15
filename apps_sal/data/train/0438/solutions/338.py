class DSU:
    
    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [1] * N
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr != yr:
            if self.size[xr] < self.size[yr]:
                xr, yr = yr, xr
            self.parents[yr] = xr
            self.size[xr] += self.size[yr]
            self.size[yr] = self.size[xr]
    
    def sz(self, x):
        return self.size[self.find(x)]

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        count = Counter()
        N = len(arr)
        S = [0] * N
        dsu = DSU(N)
        
        ans = -1
        for i, a in enumerate(arr, 1):
            a -= 1
            S[a] = 1
            
            for b in (a - 1, a + 1):
                if 0 <= b < N and S[b]:
                    count[dsu.sz(b)] -= 1
                    dsu.union(a, b)
            
            count[dsu.sz(a)] += 1
            if count[m] > 0:
                ans = i
        
        return ans
        

