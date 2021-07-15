class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        MOD = (10 ** 9) + 7
        # ways to roll target with d dice:
        # roll target - 1, -2, -3, .. , -f with d - 1 dice
        f = min(target, f)
        dp = [[0 for val in range(target+1)] for die in range(d)]
        
        for i in range(1, f+1):
            dp[0][i] = 1
            
        for i in range(1, d):
            for val in range(target+1):
                for face in range(1, f+1):
                    if val - face >= 0:
                        dp[i][val] = (dp[i-1][val-face] + dp[i][val]) % MOD
        return dp[-1][target]
