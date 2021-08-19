from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Mathematical
        # If Alex takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. At least one of first + third, second + fourth is larger, so she can always win.
        # O(1)
        # return True

        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        # N = len(piles)

        # @lru_cache(None)
        # def dp(i, j):
        #     if i > j: return 0
        #     parity = (j - i - N) % 2
        #     if parity == 1: # first player
        #         return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
        #     else:
        #         return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        # return dp(0, N - 1) > 0

        # N = len(piles)
        # dp = [[0] * N for i in range(N)]
        # for i in range(N):
        #     dp[i][i] = piles[i]
        # for d in range(1, N):
        #     for i in range(N - d):
        #         dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

        # return dp[0][-1] > 0

        N = len(piles)
        dp = piles[:]
        for d in range(1, N):
            for i in range(N - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0
