class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        num_coins = 0
        sorted_piles = list(sorted(piles))
        while len(sorted_piles):
            my_choice = sorted_piles[-2]
            num_coins += my_choice
            del sorted_piles[-2]
            del sorted_piles[0]
            del sorted_piles[-1]
        return num_coins
