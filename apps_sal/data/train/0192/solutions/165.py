class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()
        while len(piles) > 0:
            piles.pop(len(piles) - 1)
            res += piles[len(piles) - 1]
            piles.pop(len(piles) - 1)
            piles.pop(0)
        return res
