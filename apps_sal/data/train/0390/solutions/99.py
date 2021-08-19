import math


class Solution:

    def helper(self, n: int, dp: dict) -> bool:
        if n in dp:
            return dp[n]
        if n == 0:
            return False
        i = 1
        while i * i <= n:
            if self.helper(n - i * i, dp) == False:
                dp[n] = True
                return True
            i += 1
        dp[n] = False
        return False

    def winnerSquareGame(self, n: int) -> bool:
        dp = {}
        return self.helper(n, dp)
