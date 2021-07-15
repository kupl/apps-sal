class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N  = len(arr)
        umap = [list() for i in range(N)]
        dp = [-1 for i in range(N)]
        
        def dfs(idx: int) -> int:
            if idx >= N or idx < 0:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            curr = 0
            for u in umap[idx]:
                curr = max(curr, dfs(u))
            dp[idx] = curr + 1  
            
            return dp[idx]
        
        for i in range(N):
            minIdx = max(0, i-d)
            maxIdx = min(N-1, i+d)
            
            for t in range(i-1, minIdx-1, -1):
                if arr[i] > arr[t]:
                    umap[i].append(t)
                else:
                    break
                    
            for t in range(i+1, maxIdx+1):
                if arr[i] > arr[t]:
                    umap[i].append(t)
                else:
                    break
        
        result = 0
        for i in range(N):
            result = max(result, dfs(i))
            
        return result
