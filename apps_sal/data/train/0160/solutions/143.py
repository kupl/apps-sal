class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] represents for piles[i:j + 1], the maximum differnce of Alex - Lee
        n = len(piles)
        dp = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
            
        for i in range(n - 1, -1 , -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
                
        return dp[0][n - 1] > 0
