class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        res = 0
        
        while sorted_piles:
            sorted_piles.pop()
            res += sorted_piles.pop()
            sorted_piles.pop(0)
            
        return res

