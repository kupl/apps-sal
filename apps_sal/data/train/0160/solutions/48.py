class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def helper(i, j):
            if i == j:
                return piles[i]
            if (i, j) in dp:
                return dp[(i, j)] 
            
            dp[(i, j)] = max(piles[i]+helper(i+1, j), piles[j]+helper(i, j-1))
            return dp[(i , j)]

        
        if helper(0, len(piles)-1) > sum(piles)//2:
            return True
        return False
            
            

