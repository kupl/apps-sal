class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        temp = 0
        profit = 0
        r = 0
        waiting = 0
        ans = -1
        i = 0
        while i < len(customers) or waiting > 0:
            num = min(waiting + customers[i], 4) if i < len(customers) else min(waiting, 4)
            profit += num * boardingCost - runningCost
            r += 1
            waiting = max(waiting + customers[i] - 4, 0) if i < len(customers) else max(waiting - 4, 0)
            i += 1
            if profit > temp:
                temp = profit
                ans = r
        return ans
