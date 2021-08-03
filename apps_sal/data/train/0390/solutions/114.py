class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        roots = [i * i for i in range(1, int(sqrt(n)) + 1)]
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in roots:
                if i < j:
                    break

                if not dp[i - j]:
                    dp[i] = True

        return dp[n]
