class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[1] = True
        for i in range(2, n + 1):  # just to make it more clear
            k = 1
            while k * k <= i and not dp[i]:  # try to find at least one way to win
                dp[i] = not dp[i - k * k]
                k += 1
        return dp[-1]
