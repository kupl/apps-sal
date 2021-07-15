class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[[0 for i in range(2)] for z in range(len(piles))] for j in range(len(piles))]
        for i in range(len(dp)):
            dp[i][i] = [piles[i], 0]
 
        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1, len(dp[0])):
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        res = dp[0][-1]
        if dp[0][-1][0] - dp[0][-1][1] > 0:
            return True
        else:
            return False

