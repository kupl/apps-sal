class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        def is_square(num):
            a = int(num ** 0.5)
            return a * a == num
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = True
        for i in range(2, n + 1):
            dp[i] = False
            if is_square(i):
                dp[i] = True
                continue
            limit = int(i ** 0.5)
            for j in range(1, limit + 1):
                if dp[i - j * j] == False:
                    dp[i] = True
                    break
        return dp[n]
