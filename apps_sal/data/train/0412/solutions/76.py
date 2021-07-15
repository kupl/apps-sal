class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp[i][k]: the number of ways to get target \"k\" using \"i\" dices
        # dp[0][0] = 1
        # dp[i][k] = dp[i-1][k] + sum(dp[i-1][k - ff] for ff in range(1, f + 1))
        dp = [1] + [0] * target
        mod = 10**9 + 7
        for _ in range(d):
            for i in range(target, -1, -1):
                dp[i] = sum(dp[i-ff] for ff in range(1, f + 1) if i >= ff) % mod
        return dp[-1] % mod
        # for i in range(1, d + 1):
        #     for j in range(1, target + 1):
                # dp[i]
        
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                # if i == 0 and j == 0:
                #     dp[i][j] = 1
                # elif j == 0:
                #     dp[i][j] = 1
                # elif i == 0:
                #     continue
                # else:
                dp[i][j] = (sum(dp[i-1][j-ff] for ff in range(1, f + 1) if j >= ff))
        return dp[-1][-1] % mod
        
        
        # if d == 0 or target <= 0:
        #     return d == 0 and target == 0
        # res = 0
        # for i in range(1, f+1):
        #     res = (res + self.numRollsToTarget(d - 1, f, target - i)) % (10**9 + 7)
        # return res

