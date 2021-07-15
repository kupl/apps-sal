class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        dp[0]=False
        dp[1]=True
        for i in range(2,n+1):
            k=1
            while k**2<=i:
                if dp[i-k**2]==False:
                    dp[i]=True
                    break
                k+=1
        return dp[n]
