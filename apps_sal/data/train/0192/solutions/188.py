class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        
        

        return sum(piles[1:2*n//3:2])

