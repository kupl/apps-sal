class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False, True, False]
        for x in range(3, n + 1):
            dp.append(False)
            for y in range(1, n):
                a = x - y * y
                if a < 0:
                    break
                if not dp[a]:
                    dp[x] = True
                    break
        return dp[n]
