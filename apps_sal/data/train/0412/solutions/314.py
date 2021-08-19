class Solution:
    # Recursive memoized solution
    #     def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    #         memo = {}
    #         def num_rolls_util(level, target):
    #             if level * f < target or target < level:
    #                 return 0
    #             if level == 0:
    #                 return 1

    #             res = 0
    #             for i in range(max(0, target - f), target):
    #                 if (level-1, i) in memo:
    #                     res += memo[(level-1, i)]
    #                 else:
    #                     tmp = num_rolls_util(level - 1, i)
    #                     memo[(level-1, i)] = tmp
    #                     res += tmp

    #             return res % (10 ** 9 + 7)

    #         return num_rolls_util(d, target)

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, min(target, i * f) + 1):
                for k in range(1, min(j, f) + 1):
                    dp[i][j] += dp[i - 1][j - k] % mod

        return dp[d][target] % mod
