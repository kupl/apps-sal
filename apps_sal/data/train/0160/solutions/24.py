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
        #print(summ)
        if summ>sum(piles)-summ:
            return True
        return False
        '''
        n=len(piles)
        dp=[[0]*n for i in range(n)]
        #for i in range(len(piles)):
            #dp[i][i]=piles[i]
        
        for d in range(1, n): #diff between i and j is d
            for i in range(n - d):# when diff is 1, diagonally loop runs for n-1 time
                #when diff is 0, it runs for n times, ex 3X3 matrix diagonal
                j=i+d # as the diff b/w i and j is d
                if i+1==j:
                    dp[i][j] = max(piles[i],piles[j])
                else:
                    dp[i][j] = max(piles[i] + min(dp[i+2][j],dp[i+1][j-1]), piles[j] +                            min(dp[i+1][j-1],dp[i][j-2]))
        #print(dp[0][n-1])  
        return dp[0][n-1] > sum(piles) - dp[0][n-1]
        
        
        
                

