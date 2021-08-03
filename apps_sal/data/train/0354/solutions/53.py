from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache
        def roll(i, j):
            # print(i, j)
            if i == 0:
                return 1

            ans = 0
            for dice in range(6):
                if dice == j:
                    continue

                for k in range(1, min(rollMax[dice], i) + 1):
                    # print('roll', dice, k, i-k)
                    ans += roll(i - k, dice)
                    ans %= MOD
            return ans % MOD

        return roll(n, -1)


# class Solution:
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         dp = [[0] * 6 for _ in range(n+1)]
#         dp[1] = [1] * 6
#         # print(dp[1])

#         for i in range(2, n+1):
#             for j in range(6):
#                 pi = i - rollMax[j]
#                 if pi < 1:
#                     dp[i][j] = sum(dp[i-1])
#                 elif pi == 1:
#                     dp[i][j] = sum(dp[i - 1]) - 1
#                 elif pi > 1:
#                     dp[i][j] = sum(dp[i - 1]) - sum(dp[pi-1][:j] + dp[pi-1][j + 1:])
#                 dp[i][j] = dp[i][j] % (10**9 + 7)
#             # print(dp[i])
#         return sum(dp[-1]) % (10**9 + 7)
