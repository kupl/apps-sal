import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            curr = 1
            while curr**2 <= i:
                if dp[i - curr**2] == False:
                    dp[i] = True
                    break
                curr += 1
        return dp[-1]
