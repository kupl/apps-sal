class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        for i in range(1, n + 1):
            base = 1
            while i - base**2 >= 0:
                if not dp[i - base**2]:
                    dp[i] = True
                    break
                else:
                    base += 1
        return dp[n]
