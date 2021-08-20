class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for k in range(1, int(i ** 0.5) + 1):
                if i - k ** 2 < 0:
                    break
                if not dp[i - k ** 2]:
                    dp[i] = True
                    break
        return dp[-1]
        '\n        dp = [False] * (n + 1)\n        for i in range(1, n + 1):\n            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))\n        return dp[-1]   \n        '
