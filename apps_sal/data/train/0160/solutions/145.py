class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = piles[i]
        s = sum(piles)
        
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(piles[i] + s - dp[i+1][j], piles[j] + s - dp[i][j-1])
                
        return dp[0][n - 1] > (s // 2)
