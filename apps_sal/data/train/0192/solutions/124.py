class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        numCoins = 0
        piles.sort()

        while len(piles) > 0:
            piles.pop()
            numCoins += piles.pop()
            piles.pop(0)

        return numCoins
