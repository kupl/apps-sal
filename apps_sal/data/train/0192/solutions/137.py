class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        sorted_piles = sorted(piles)
   
        while len(sorted_piles):
            sorted_piles.pop()
            coins += sorted_piles.pop()
            sorted_piles.pop(0)
            
            
        return coins
