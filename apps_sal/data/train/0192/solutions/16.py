class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        coins = 0
        for i in range(len(piles) // 3, len(piles), 2):
            coins += piles[i]
        return coins
