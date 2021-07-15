class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        par = {}
        sz = {}
        target = set()
        
        def find(i):
            while i != par[i]:
                par[i] = par[par[i]]
                i = par[i]
            return i
        
        def union(i, j):
            x = find(i)
            y = find(j)
            if x == y:
                return
            if sz[x] <= sz[y]:
                sz[y] += sz[x]
                par[x] = y
                
                if sz[y] == m:
                    target.add(y)
                    
                if sz[x] == m and x in target:
                    target.remove(x)
            else:
                sz[x] += sz[y]
                par[y] = x
                
                if sz[x] == m:
                    target.add(x)
                    
                if sz[y] == m and y in target:
                    target.remove(y)
        
        count = 1
        ans = -1
        for i in arr:
            if i not in par:
                par[i] = i
                sz[i] = 1
                if m == 1:
                    target.add(i)
                
            if i - 1 in par and i + 1 in par:
                union(i-1, i+1)
                union(i-1, i)
            elif i - 1 in par:
                union(i-1, i)
            elif i + 1 in par:
                union(i, i+1)
                
            t = set()
            for i in target:
                if sz[i] == m:
                    ans = count
                    t.add(i)
            target = t
            count += 1
                
        return ans
            

