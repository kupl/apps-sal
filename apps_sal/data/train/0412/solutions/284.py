class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > f*d:
            return 0
        
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        
        for i in range(d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if k > j:
                        continue
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k])%(10 ** 9 + 7)
        
        return dp[-1][-1]

