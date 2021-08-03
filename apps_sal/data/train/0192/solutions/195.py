class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me_max = 0
        start = len(piles) - 2
        for i in range(int(len(piles) / 3)):
            idx = start - (2 * i)
            me_max += piles[idx]
        return me_max
