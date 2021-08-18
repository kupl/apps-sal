class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        i = len(piles) - 2
        while i >= int(len(piles) / 3):
            result += piles[i]
            i -= 2
        return result
