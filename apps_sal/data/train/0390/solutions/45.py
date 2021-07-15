class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]
        i = 0
        while i*i <= n:
            dp[i*i] = True  # next round is Alice, she wins immediately
            i += 1
        for i in range(1, n+1):
            k = 1
            while k*k <= i and not dp[i]:
                dp[i] = not dp[i-k*k]
                k += 1
        return dp[-1]

