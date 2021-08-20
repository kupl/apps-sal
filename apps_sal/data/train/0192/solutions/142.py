class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        s = len(piles) // 3
        n = len(piles)
        (i, j, k) = (0, n - 2, n - 1)
        sumi = 0
        while s != 0:
            sumi += piles[j]
            j = j - 2
            s = s - 1
        return sumi
