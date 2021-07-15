class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = {}
        
        for i in range(n):
            dp[(i,i)] = [piles[i],0]
        
        for i in range(n - 2, - 1,-1):
            for j in range(i + 1,n):
                left = [dp[(i + 1,j)][1] + piles[i],dp[(i + 1,j)][0]]
                right = [dp[(i,j - 1)][1] + piles[j],dp[(i,j - 1)][0]]

                dp[(i,j)] = max ( left ,right)         
        return dp[(0,n - 1)][0] > dp[(0,n - 1)][1]
