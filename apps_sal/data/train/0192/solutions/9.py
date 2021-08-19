class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 2
        total = 0
        while left < right:
            total += piles[right]
            left += 1
            right -= 2
        return total
