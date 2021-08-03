class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        result = 0
        for idx in range(1, 2 * len(piles) // 3 + 1, 2):
            result += piles[idx]
        return result
