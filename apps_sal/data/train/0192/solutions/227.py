class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        n = len(piles) // 3
        m = len(piles) - 1
        for i in range(m, n, -2):
            total += piles[i - 1]
        return total
