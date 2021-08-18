class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        me = 0
        start, end = 0, len(piles) - 1
        while start < end:
            if end - 1 > 0:
                me += piles[end - 1]
            start, end = start + 1, end - 2
        return me
