class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 3)
        dp[1] = 1
        dp[2] = 0

        for i in range(3, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if j**2 <= i:
                    if dp[i - j**2] == 0:
                        dp[i] = 1
                        break

        print((dp[n]))
        return dp[n] == 1
