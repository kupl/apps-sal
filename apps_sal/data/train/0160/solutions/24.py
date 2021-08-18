class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        def helper(piles,i,j):
            if i==j:
                return piles[i]
            elif i+1==j:
                return max(piles[i],piles[j])
            return max(piles[i]+min(helper(piles,i+2,j),helper(piles,i+1,j-1)), piles[j]+
            min(helper(piles,i+1,j-1),helper(piles,i,j-2)))
        summ=helper(piles,0,len(piles)-1)
        if summ>sum(piles)-summ:
            return True
        return False
        '''
        n = len(piles)
        dp = [[0] * n for i in range(n)]

        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                if i + 1 == j:
                    dp[i][j] = max(piles[i], piles[j])
                else:
                    dp[i][j] = max(piles[i] + min(dp[i + 2][j], dp[i + 1][j - 1]), piles[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
        return dp[0][n - 1] > sum(piles) - dp[0][n - 1]
