class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factorize(m, val, idx):
            for i in range(1, math.floor(math.sqrt(val) + 1)):
                f = val // i
                if f * i == val:
                    m[i].append(idx)
                    m[f].append(idx)
            return
        
        n = len(A)
        m = defaultdict(list)
        for idx, val in enumerate(A):
            factorize(m, val, idx)
        
        al = [[] for _ in range(n)]
        for k in m:
            if k == 1: continue
            vals = m[k]
            for idx in range(len(vals) - 1):
                al[vals[idx]].append(vals[idx+1])
                al[vals[idx+1]].append(vals[idx])
                
        v = [False]*n
            
        def dfs(val):
            # print(f\"dfs: {val}\")
            if v[val]:
                return 0
            res = 1
            v[val] = True
            for nei in al[val]:
                res += dfs(nei)
            return res
        
        max_csize = 0
        # print(al)
        for idx in range(n):
            if not v[idx]:
                # print(f\"{idx}: {max_csize}\")
                max_csize = max(max_csize, dfs(idx))
                # print(f\"{idx}: {max_csize}\")
        return max_csize
        
        

