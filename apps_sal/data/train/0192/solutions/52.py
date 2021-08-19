class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        coins = sorted(piles)
        me = 0
        for piles in range(int(len(coins) / 3), len(coins), 2):
            me += coins[piles]
        return me
