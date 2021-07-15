class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, key=lambda x: -x)
        total = 0
        for i in range(0, len(piles) * 2 // 3, 2):
            total += piles[i + 1]
        return total
