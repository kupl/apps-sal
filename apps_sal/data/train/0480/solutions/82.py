LIMIT = 10**9 + 7

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_pos = min(steps // 2 + 1, arrLen) + 1
        dp = [[0] * max_pos for _ in range(steps)]
        dp[0][0] = dp[0][1] = 1
        
        for i in range(1, steps):
            for j in range(max_pos-1):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]) % LIMIT
            
        return dp[-1][0]
    
# time: O(min(arrLen, steps) * steps)
# space: O(min(arrLen, steps) * steps)

