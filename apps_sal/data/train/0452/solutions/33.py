# 11:19 - 
class Solution:
    def minDifficulty(self, difficulty: List[int], d: int) -> int:
        # dp[n, d] = dp[n - 1, d - i] + max(n - i, n) 
        if d > len(difficulty):
            return -1
        
        n = len(difficulty)
        dp = [[float('inf')] * (n + 1) for _ in range(2)]
        dp[1][0] = 0
        
        # dp[i, j]: finish 'j' jobs in 'i' days
        for i in range(d):
            for j in range(n):
                dp[i & 1][j + 1] = float('inf')
                local = float('-inf')
                for k in range(j, -1, -1):
                    if k < i:
                        break
                    local = max(local, difficulty[k])
                    dp[i & 1][j + 1] = min(dp[i & 1][j + 1], local + dp[(i + 1) & 1][k])
        
        return dp[(d - 1) & 1][-1]

