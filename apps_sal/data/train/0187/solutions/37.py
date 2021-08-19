class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        step = -1
        waiting = 0
        cur_profit = 0
        i = 0
        for customer in customers:
            i += 1
            if customer > 4:
                waiting += customer - 4
                cur_profit += 4 * boardingCost - runningCost
            else:
                waiting += customer
                if waiting >= 4:
                    cur_profit += 4 * boardingCost - runningCost
                    waiting -= 4
                else:
                    cur_profit += waiting * boardingCost - runningCost
                    waiting = 0
            if cur_profit > max_profit:
                max_profit = cur_profit
                step = i
        while waiting > 0:
            i += 1
            if waiting >= 4:
                cur_profit += 4 * boardingCost - runningCost
                waiting -= 4
            else:
                cur_profit += waiting * boardingCost - runningCost
                waiting = 0
            if cur_profit > max_profit:
                max_profit = cur_profit
                step = i
        return step
