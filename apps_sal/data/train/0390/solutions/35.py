class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[1] = True
        for i in range(2, n + 1):
            k = 1
            while k * k <= i and not dp[i]:
                dp[i] = not dp[i - k * k]
                k += 1
        return dp[-1]
