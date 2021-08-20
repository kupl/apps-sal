class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        i = 1
        res = 0
        while i < 2 * n:
            res += piles[i]
            i += 2
        return res
