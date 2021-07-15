class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        piles = piles[n:] # remove Bob's
        return sum(piles[i*2] for i in range(n))
