class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False for i in range(n + 1)]
        sqs = [i * i for i in range(1, 1 + int(math.sqrt(n)))]
        for i in range(n + 1):
            t = False
            for sq in sqs:
                if i - sq < 0:
                    break
                if not dp[i - sq]:
                    t = True
                    break
            dp[i] = t

        return dp[n]
