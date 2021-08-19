class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(reverse=True)
        for i in range(len(piles) // 3):
            res += piles[2 * (i + 1) - 1]
        return res
