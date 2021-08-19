class Solution:

    def maxCoins(self, piles):
        piles.sort(reverse=True)
        return sum(piles[1:int(len(piles) / 3 * 2) + 1:2])
