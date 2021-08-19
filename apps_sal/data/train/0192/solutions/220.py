import heapq


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        piles = piles[len(piles) // 3:]
        me = 0
        for i in range(len(piles) - 2, -1, -2):
            me += piles[i]
        return me
