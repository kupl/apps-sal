class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxCoins = 0
        count = len(piles)
        while count > 0:
            piles.pop(0)
            maxCoins += piles.pop(-2)
            piles.pop(-1)
            count = len(piles)
        return maxCoins
