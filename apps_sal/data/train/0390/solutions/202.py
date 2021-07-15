class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                dp[i] |= not dp[i-j*j]
                j+=1
        return dp[n]

