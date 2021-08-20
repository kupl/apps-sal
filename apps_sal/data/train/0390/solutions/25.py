from collections import deque


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for x in range(2, n + 1):
            i = 1
            while i * i <= x:
                if not dp[x - i * i]:
                    dp[x] = True
                    break
                i += 1
        return dp[n]
