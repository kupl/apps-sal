class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:  return -1
        max_profit, cur_profit, waiting, i = 0, 0, 0, 0
        res = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
            i += 1
            boarded = min(waiting, 4)
            cur_profit += boarded * boardingCost - runningCost
            #print(waiting, boarded, cur_profit, max_profit)
            if cur_profit > max_profit:
                res = i
                max_profit = cur_profit
            waiting -= boarded
        return res

