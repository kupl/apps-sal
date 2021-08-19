class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        l = len(piles) // 3
        piles.sort()
        piles = piles[l:]
        r = 0
        for (m, i) in enumerate(piles):
            if m % 2 == 0:
                r += i
        return r
