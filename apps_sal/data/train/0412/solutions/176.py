class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(target + 1)] for i in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for val in range(1, f + 1):
                    if j - val >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % (10 ** 9 + 7)
        return dp[-1][-1] % (10 ** 9 + 7)
        
        

