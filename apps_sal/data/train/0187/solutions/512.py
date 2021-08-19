class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = [0]
        person_remain = customers[0]
        i = 1
        while person_remain or i == 1:
            gondola = min(4, person_remain)
            profits.append(gondola * boardingCost - runningCost + profits[-1])
            person_remain = person_remain - gondola
            if i < len(customers):
                person_remain += customers[i]
            i += 1
        max_round = 0
        max_el = max(profits)
        if max_el <= 0:
            return -1
        for i in range(len(profits)):
            if profits[i] == max_el:
                max_round = i
                break
        return max_round
