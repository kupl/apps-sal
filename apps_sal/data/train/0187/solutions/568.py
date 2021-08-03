class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        maxProfit = -1
        res = -1
        currentCustomer = 0
        for i, c in enumerate(customers):
            currentCustomer += c
            if currentCustomer <= 4:
                profit += currentCustomer * boardingCost - runningCost
                currentCustomer = 0
            else:
                profit += 4 * boardingCost - runningCost
                currentCustomer -= 4
            if profit > maxProfit:
                maxProfit = profit
                res = i + 1

        rounds = currentCustomer // 4
        left = currentCustomer % 4
        if boardingCost * 4 - runningCost > 0:
            profit += rounds * (boardingCost * 4 - runningCost)
            if profit > maxProfit:
                maxProfit = profit
                res += rounds
            profit += boardingCost * left - runningCost
            if profit > maxProfit:
                maxProfit = profit
                res += 1

        return res
