class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)

        for i in reversed(range(n)):
            temp = 1
            while i + temp * temp <= n:
                j = i + temp * temp
                temp += 1
                if not dp[j]:
                    dp[i] = True
                    break

        return dp[0]
