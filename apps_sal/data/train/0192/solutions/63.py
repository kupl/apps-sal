class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        i = 1
        for j in range(len(piles) // 3):
            res += piles[i]
            i += 2
        return res
