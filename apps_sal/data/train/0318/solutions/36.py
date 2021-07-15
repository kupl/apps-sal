class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        N = len(slices)
        target = N//3
        dp = [[-1 for x in range(target)] for y in range(N)]
        
        def dfs(idx: int, cnt: int) -> int:
            if cnt >= target or idx >= N:
                return 0
            
            if dp[idx][cnt] == -1:
                dp[idx][cnt] = max(dfs(idx+1, cnt), slices[idx]+dfs(idx+2, cnt+1))
            return dp[idx][cnt]
            
        result = dfs(1, 0)
        dp = [[-1 for x in range(target)] for y in range(N)]
        N -= 1
        result = max(result, dfs(0, 0))
        
        return result
