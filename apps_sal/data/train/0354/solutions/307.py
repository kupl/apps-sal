class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        
        dp = [[0 for _ in range(len(rollMax) + 1)] for _ in range(n + 1)]
        
        dp[0][-1] = 1
        dp[1] = [1] * len(rollMax) + [len(rollMax)]
        for i in range(2, n + 1):
            for j in range(len(rollMax)):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0: break
                    dp[i][j] += dp[i-k][-1] - dp[i-k][j]
            dp[i][-1] = sum(dp[i])
        return dp[-1][-1]% 1000000007
