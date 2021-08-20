class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        res = 0
        for i in range(len(piles) - 2, len(piles) - 2 - n * 2, -2):
            res += piles[i]
        return res
