class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i**0.5 == int(i**0.5):
                dp[i] = 1
                continue
            else:
                for j in range(1, int(i**0.5) + 1):
                    if dp[i - j**2] == 0:
                        dp[i] = 1
                        break
        return bool(dp[n])
