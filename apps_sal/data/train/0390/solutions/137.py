class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1,n+1):
            cur = int(i**0.5)
            if cur ** 2 == i:
                dp[i] = True
            else:
                f = True
                for j in range(1,int(i**0.5)+1):
                    f &= dp[i-j*j]
                if not f:
                    dp[i] = True
        return dp[-1]
