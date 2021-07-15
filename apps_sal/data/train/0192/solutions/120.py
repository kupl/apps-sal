class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_coins = 0
        piles = sorted(piles)
        while piles:
            del piles[0]
            del piles[-1]
            my_coins += piles[-1]
            del piles[-1]
        return my_coins

