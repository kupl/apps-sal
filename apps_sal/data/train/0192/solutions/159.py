class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxCoins = 0
        while len(piles) > 0:
            piles.pop()
            maxCoins += piles.pop()
            piles.pop(0)
        return maxCoins
