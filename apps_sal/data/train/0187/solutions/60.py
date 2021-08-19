class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        rotations = -1
        maxProfit = 0
        waiting = 0
        profit = 0
        i = 0
        while True:
            if i < len(customers):
                waiting += customers[i]
            elif waiting == 0:
                break
            i += 1
            if waiting > 4:
                waiting -= 4
                profit += 4 * boardingCost - runningCost
            else:
                profit += waiting * boardingCost - runningCost
                waiting = 0
            if profit > maxProfit:
                maxProfit = profit
                rotations = i
        return rotations
