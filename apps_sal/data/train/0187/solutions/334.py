class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        minOp = currCustomers = profit = maxProfit = i = totalCustomers = 0
        while customers[-1] == 0:
            customers.pop()
        for c in customers:
            i += 1
            currCustomers += c
            totalCustomers += min(4, currCustomers)
            profit = boardingCost * totalCustomers - (i + 1) * runningCost
            currCustomers -= min(4, currCustomers)
            if profit > maxProfit:
                maxProfit = profit
                minOp = i
        while currCustomers:
            i += 1
            totalCustomers += min(4, currCustomers)
            profit = boardingCost * totalCustomers - (i + 1) * runningCost
            currCustomers -= min(4, currCustomers)
            if profit > maxProfit:
                maxProfit = profit
                minOp = i
        return minOp if maxProfit > 0 else -1
