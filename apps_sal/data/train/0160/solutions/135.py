class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # condition on first dp[i,j] is the number of stones greater than the opponent if both using the optimum strate
        # take first, dp[0][n-1] = max(piles[0] - dp[1][n-1], piles[n-1] - dp[0][n-2])
        # dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j+1]
        # return dp[0][n-1]
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        
        # initialize
        for i in range(n):
            dp[i][i] = piles[i]
            
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
            # print(dp)
            
        return dp[0][n-1] > 0
