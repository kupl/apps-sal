class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        for i in range(1, n + 1):
            for e in range(1, int(i ** 0.5) + 1):
                if not dp[i - e ** 2]:
                    dp[i] = True
                    break
        return dp[-1]
