class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        rounds = len(piles) // 3
        count = 0
        piles.sort(reverse=True)
        for i in range(0, 2 * rounds, 2):
            count += piles[i + 1]
        return count
