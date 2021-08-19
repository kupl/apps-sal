class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        ans = 0
        max_profit = 0
        wait = 0
        curr = 0
        for c in customers:
            wait += c
            if wait <= 4:
                profit += wait * boardingCost - runningCost
                wait = 0
            else:
                profit += 4 * boardingCost - runningCost
                wait -= 4
            curr += 1
            if profit > max_profit:
                max_profit = profit
                ans = curr
        while wait > 0:
            if wait <= 4:
                profit += wait * boardingCost - runningCost
                wait = 0
            else:
                profit += 4 * boardingCost - runningCost
                wait -= 4
            curr += 1
            if profit > max_profit:
                max_profit = profit
                ans = curr
        if max_profit <= 0:
            return -1
        else:
            return ans
