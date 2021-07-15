class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = piles[i]
        cum = [0] * n
        cum[0] = piles[0]
        for i in range(1, n):
            cum[i] = cum[i-1] + piles[i]
        
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(piles[i] + cum[n-1] - dp[i+1][j], piles[j] + cum[n-1] - dp[i][j-1])
                
        return dp[0][n - 1] > (cum[n-1] // 2)
