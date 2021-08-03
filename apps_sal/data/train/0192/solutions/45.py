class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        n = len(piles)
        cost = 0
        left = 0
        right = n - 1
        for _ in range(n // 3):
            cost += piles[right - 1]
            left += 1
            right -= 2
        return cost
