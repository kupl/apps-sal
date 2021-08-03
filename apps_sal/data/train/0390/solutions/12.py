class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp, sqs = [False] * (n + 1), []
        i = 1
        while i * i <= n:
            sqs.append(i * i)
            i += 1
        for i in range(1, n + 1):
            for sq in sqs:
                if sq > i:
                    break
                dp[i] = dp[i] or not dp[i - sq]
                if dp[i]:
                    break
        return dp[n]
