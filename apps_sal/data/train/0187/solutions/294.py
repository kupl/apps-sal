class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        wait = customers[0]
        boarded = 0
        profit = 0
        res = -1
        index = 0
        while wait > 0 or index < len(customers):
            if index and index < len(customers):
                wait += customers[index]
            onboard = min(4, wait)
            boarded += onboard
            wait -= onboard
            if boarded * boardingCost - (index + 1) * runningCost > profit:
                res = index + 1
                profit = boarded * boardingCost - (index + 1) * runningCost
            index += 1
        return res
