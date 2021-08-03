class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        res, l, r = 0, 0, len(piles) - 1
        # round
        while l < r:
            l += 1
            r -= 1
            res += piles[r]
            r -= 1
        return res
