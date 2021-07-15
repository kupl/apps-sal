class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for interval in range(1,n):
            for left in range(n-interval):
                dp[left][left+interval] = max(piles[left]-dp[left+1][left+interval],piles[left+interval] - dp[left][left+interval-1])
        return dp[0][-1]>0
