class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort pile from least to greatest
        sorted_piles = piles
        sorted_piles.sort()

        max_coins = 0
        num_groups = int(len(sorted_piles) / 3)

        for i in range(num_groups):
            sorted_piles.pop(len(sorted_piles) - 1)  # pop last element
            sorted_piles.pop(0)                     # pop first element
            your_coin = sorted_piles.pop(len(sorted_piles) - 1)
            max_coins += your_coin

        return max_coins
