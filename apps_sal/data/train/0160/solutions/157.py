class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i]=piles[i]
        for m in range(2,n+1):
            for l in range(n-m+1):
                r=l+m-1
                dp[l][r]=max(piles[l]-dp[l+1][r], piles[r]-dp[l][r-1])
        return dp[0][n-1]>0
