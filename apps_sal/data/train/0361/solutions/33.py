class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = n*m
        
        def dfs(hts, mvs):
            if mvs >= self.best: return
            if all(h==n for h in hts): 
                self.best = min(self.best, mvs)
                return
            i = min(list(range(m)), key=lambda i:hts[i])
            j = i + ([hts[k] != hts[i] for k in range(i,m)] + [True]).index(True)
            # while j < m and hts[j] == hts[i]: j+=1
            for x in range(min(j-i, n-hts[i]), 0, -1):
                for k in range(x):
                    hts[i+k] += x
                dfs(hts, mvs+1)
                for k in range(x):
                    hts[i+k] -= x
        
        dfs([0]*m, 0)
        return self.best
            
            
            
                

