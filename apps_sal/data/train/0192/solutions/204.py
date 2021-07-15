class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        piles.sort()
        piles=piles[n::2]
        return sum(piles)

