class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        res = 0
        n = len(piles)
        n = n // 3
        for i in range(1, 2 * n, 2):
            res += piles[i]
        return res
