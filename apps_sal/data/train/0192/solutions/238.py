class Solution:
    def maxCoins(self, piles):
        piles.sort()
        end = len(piles) - 2
        start = 0
        count = 0
        while start < end:
            count += piles[end]
            end -= 2
            start += 1
        return count
