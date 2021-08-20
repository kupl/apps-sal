class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = {}

        def rec_win(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n in dp:
                return dp[n]
            for i in range(1, n):
                if i * i > n:
                    break
                if not rec_win(n - i * i):
                    dp[n] = True
                    return True
            dp[n] = False
            return False
        return rec_win(n)
