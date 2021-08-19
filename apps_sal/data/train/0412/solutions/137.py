class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def dfs(d, target):
            if (d, target) in cache:
                return cache[(d, target)]
            if target < 0 or d < 0:
                return 0
            if target == 0 and d == 0:
                return 1
            ways = 0
            for i in range(1, f + 1):
                ways += dfs(d - 1, target - i)
            cache[(d, target)] = ways
            return ways

        cache = {}
        mod = 10 ** 9 + 7
        return dfs(d, target) % mod

        # mod = 10 ** 9 + 7
        # dp = [[0] * (target + 1) for _ in range(d + 1)]
        # # dp[0][0] = 1
        # for i in range(1, min(f, target) + 1):
        #     dp[1][i] = 1
        # for i in range(2, d + 1):
        #     # the numbers that can be reached by rolling i dice
        #     for num in range(i, min(i * f, target) + 1):
        #         for diceNum in range(1, (f + 1)):
        #             if num - diceNum >= 1:
        #                 dp[i][num] += dp[i - 1][num - diceNum]
        #             else:
        #                 break
        # return dp[d][target] % mod
