class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = {0: False}
        for i in range(0, n):
            if i in dp and i != 0:
                continue
            for j in range(1, n + 1):
                if i + j * j > n:
                    break
                dp[i + j * j] = True
        return False if n not in dp else dp[n]
