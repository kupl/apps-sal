class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[int(len(piles)/3)::2])

