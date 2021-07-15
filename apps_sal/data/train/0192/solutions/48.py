class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        n = len(piles)
        s = 0
        for i in range(n // 3):
            s += piles[n-1-(2*i+1)]
        return s

