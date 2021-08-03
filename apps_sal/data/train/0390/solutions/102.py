class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        if n == 0 or n == 2:
            return False
        if n == 1:
            return True
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 0

        def pick(n):

            if dp[n] != -1:
                return dp[n]
            i = 1
            while i * i <= n:
                if i * i == n:
                    dp[n] = 1
                    return True
                if not pick(n - i * i):
                    dp[n] = 1
                    return True
                i = i + 1
            dp[n] = 0
            return dp[n]
        pick(n)
        return dp[n] == 1
