class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit = -1
        profit = 0
        i = 0
        res = 0
        ans = 0
        for i in range(len(customers)):
            customers[i] += res
            if customers[i] > 4:
                res = customers[i] - 4
                profit += 4 * boardingCost - runningCost
            else:
                res = 0
                profit += customers[i] * boardingCost - runningCost
            if profit > maxProfit:
                maxProfit = profit
                ans = i + 1

        step = 1
        while res > 0:
            if res > 4:
                profit += 4 * boardingCost - runningCost
            else:
                profit += res * boardingCost - runningCost
            res -= 4
            if profit > maxProfit:
                maxProfit = profit
                ans = len(customers) + step
            step += 1

        if maxProfit <= 0:
            return -1

        return ans
