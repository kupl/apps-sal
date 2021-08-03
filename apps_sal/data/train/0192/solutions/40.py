class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[int(len(piles) / 3)::2])
