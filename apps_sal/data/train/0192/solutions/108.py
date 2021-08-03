class Solution:
    def maxCoins(self, piles):
        choose = 0
        piles = sorted(piles, reverse=True)
        for i in range(len(piles) // 3):
            choose += piles[2 * i + 1]
        return choose
