class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count_total = 0
        while len(piles) > 0:
            max_el = piles.pop(-1)
            second_max_el = piles.pop(-1)
            min_el = piles.pop(0)
            count_total += second_max_el
        return count_total
