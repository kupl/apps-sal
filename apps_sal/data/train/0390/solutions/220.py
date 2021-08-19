class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        square = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [False for i in range(n + 1)]
        dp[1] = True
        dp[0] = False
        for i in range(2, n + 1):
            for sq in square:
                if sq > i:
                    break
                if not dp[i - sq]:
                    dp[i] = True
                    break
        return dp[-1]
