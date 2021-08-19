class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        i = len(piles) - 2
        count = 1
        while count <= len(piles) / 3:
            res += piles[i]
            i -= 2
            count += 1
        return res
