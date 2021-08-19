class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        return sum([piles[len(piles) - 2 - 2 * i] for i in range(0, n)])
