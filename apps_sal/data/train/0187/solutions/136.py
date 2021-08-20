class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        result = 0
        totalPeople = 0
        totalProfit = 0
        maxProfit = 0
        for (i, num) in enumerate(customers):
            totalPeople += num
            onBoard = min(4, totalPeople)
            totalPeople -= onBoard
            totalProfit += onBoard * boardingCost - runningCost
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                result = i + 1
        (q, r) = divmod(totalPeople, 4)
        if 4 * boardingCost > runningCost:
            result += q
        if r * boardingCost > runningCost:
            result += 1
        return result if result > 0 else -1
