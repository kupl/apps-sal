class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        your_total = 0
        while sorted_piles:
            sorted_piles.pop(0)
            sorted_piles.pop(-1)
            your_total += sorted_piles.pop(-1)
        return your_total
