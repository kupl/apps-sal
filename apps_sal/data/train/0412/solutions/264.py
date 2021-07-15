class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # Dynamic programming on the number of dice?
        # if i have n - 1 dice, and know the number of ways to get to all possible targets
        # then i should be able to compute the number of way to get to a target with n dice
        
       # keep a vector of number of ways to get to targets between 1 and \"target\" for d = 1 etc
    
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                    k += 1
        return dp[d][target] % mod

