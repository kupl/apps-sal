class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        count_total = 0

        while len(piles) > 0:

            max_el = piles.pop(-1)
            # print(\"max_el is \" + str(max_el))
            second_max_el = piles.pop(-1)
            # print(\"second_max_el is \" + str(second_max_el))
            min_el = piles.pop(0)
            # print(\"min_el is \" + str(min_el))

            count_total += second_max_el

        return count_total
