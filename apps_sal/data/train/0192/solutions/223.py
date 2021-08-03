class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        mc = 0
        piles.sort(reverse=True)
        print(piles)
        for i in range(0, n):
            mc += piles[1 + 2 * i]
        return mc
