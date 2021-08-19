class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        dp = [None] * (n + 1)
        (dp[0], dp[1], dp[2]) = (False, True, False)
        for i in range(3, n + 1):
            for j in range(1, n * n):
                y = i - j * j
                if y < 0:
                    break
                if not dp[y]:
                    dp[i] = True
                    break
        return dp[-1]
