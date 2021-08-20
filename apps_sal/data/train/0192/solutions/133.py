class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        max_coins_for_me = 0
        sorted_piles = sorted(piles)
        while len(sorted_piles) > 0:
            alice = sorted_piles.pop()
            max_coins_for_me += sorted_piles.pop()
            bob = sorted_piles.pop(0)
        return max_coins_for_me
