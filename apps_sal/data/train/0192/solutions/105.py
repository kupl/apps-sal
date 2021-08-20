class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        l = len(piles) // 3
        p = len(piles) - l
        s = sum([piles[i] for i in range(1, p, 2)])
        return s
