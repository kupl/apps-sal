class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) == 3:
            return piles[1]
        return sum((a for a in sorted(piles)[len(piles) // 3::2]))
