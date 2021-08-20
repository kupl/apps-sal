class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        waiting = 0
        rotation = 0
        max_profit = 0
        ans = None
        for customer in customers:
            customer += waiting
            rotation += 1
            if customer >= 4:
                profit += 4 * boardingCost - runningCost
                waiting = customer - 4
            else:
                profit = customer * boardingCost - runningCost
                waiting = 0
            if max_profit < profit:
                max_pprofit = profit
                ans = rotation
        if 4 * boardingCost - runningCost > 0:
            steps = waiting // 4
            profit += steps * (4 * boardingCost - runningCost)
            waiting = waiting - steps * 4
            if waiting * boardingCost - runningCost > 0:
                profit += waiting * boardingCost - runningCost
                steps += 1
            if max_profit < profit:
                max_pprofit = profit
                ans = rotation + steps
        return ans if ans else -1
