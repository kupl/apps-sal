class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        Count = 0
        
        while piles:
            
            Count += piles[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
            
        return Count
