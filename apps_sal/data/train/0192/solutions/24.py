class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # [2,4,1,2,7,8]
        # [1,2,2,4,7,8]
        piles.sort()
        n = len(piles)
        
        if n < 3:
            return 0
        
        current = n - 2
        low = 0
        total = 0
        
        while current > low:
            total += piles[current]
            current -= 2
            low += 1
            
        return total
        
        

