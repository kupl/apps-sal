import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        return self.alice_wins(n, {})

    def alice_wins(self, n, dp):
        if n in dp:
            return dp[n]
        x = 1
        dp[n] = False
        while x * x <= n:
            if not self.alice_wins(n - x * x, dp):
                dp[n] = True
                break
            x += 1
        return dp[n]


'\nAlice tries to get to 0 first\nBob tries to get to get to 0 first/ Bob tries to not allow Alice get to zero first\n\n\n\n37\n\n\nAlice tries all perfect squares\nIf current num is perfect square, Bob picks it, else he picks 1\n'
