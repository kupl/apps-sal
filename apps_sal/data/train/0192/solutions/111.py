class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        max_index = len(piles) - 2
        result = 0
        piles.sort()
        for _ in range(len(piles) // 3):
            result += piles[max_index]
            max_index -= 2
        return result
