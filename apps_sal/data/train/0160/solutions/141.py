class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Let f(i,j) be the maximum difference Alex-Lee
        # Key idea: If Alex takes pile[i], then Lee will play optimally to get a score of f(i+1, j) for him,
        # which is equilvalent to Alex getting a score of -f(i+1, j). So Alex's total score is pile[i] - f(i+1,j)
        # Then just take the pile that results in maximum score.
        # f(i,j) = max(piles[i] - f(i+1,j), piles[j] - f(i,j-1))
        # Base case: f(i,i) = piles[i]
        # If you draw the 2d grid, it looks like filling in diagonal order
        # Can do space optimization using 1D DP
        n = len(piles)
        if n == 1:
            return True
        
        # First let's do 2D DP, space optimize later
        dp = [[None]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
                
        return dp[0][n-1] > 0
