class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        steps = int(len(piles)/3)
        piles = sorted(piles)
        
        return sum(piles[steps::2])
