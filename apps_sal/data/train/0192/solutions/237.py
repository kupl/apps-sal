class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        p = piles[len(piles) - 2::-2]
        return sum(p[:len(piles) // 3])
