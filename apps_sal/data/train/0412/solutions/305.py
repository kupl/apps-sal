class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target:
            return 0
        elif d * f == target:
            return 1
        
        dp = [[0] * (target+1) for _ in range(d)] # dp[i][j]: solution for target j with i + 1 dices
        BASE = 10**9 + 7
        for j in range(1, min(f, target)+1):
            dp[0][j] = 1
        for i in range(1, d):
            for j in range(target+1):
                for k in range(1, f+1):
                    if k >= j: break
                    dp[i][j] += dp[i-1][j-k] % BASE
        
        return dp[d-1][target] % BASE
