class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        result = 0
        piles.sort(reverse=True)
        for i in range(n // 3):
            result += piles[i * 2 + 1]

        return result
