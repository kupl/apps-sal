class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        boarded = 0
        maxProfit = 0
        maxIndex = -1

        if len(customers) == 0:
            return -1

        for i, customerCount in enumerate(customers):
            waiting += customerCount
            if waiting >= 4:
                waiting -= 4
                boarded += 4
            else:
                boarded += waiting
                waiting = 0

            profit = boarded * boardingCost - (i + 1) * runningCost
            if profit > maxProfit:
                maxIndex = i + 1
                maxProfit = profit

        i += 1
        while waiting > 0:
            if waiting >= 4:
                waiting -= 4
                boarded += 4
            else:
                boarded += waiting
                waiting = 0

            profit = boarded * boardingCost - (i + 1) * runningCost
            if profit > maxProfit:
                maxIndex = i + 1
                maxProfit = profit
            i += 1

        if maxProfit > 0:
            return maxIndex
        return -1
