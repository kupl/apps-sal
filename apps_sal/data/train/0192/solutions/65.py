class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret = 0
        left = 0
        right = len(piles) - 1

        while (left < right):
            ret += piles[right - 1]
            left += 1
            right -= 2

        return ret
