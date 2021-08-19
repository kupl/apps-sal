class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        # [1,2,3,4,5,6,7,8,9]
        for i in range(len(piles) - 2, len(piles) // 3 - 1, -2):
            total += piles[i]

        return total
