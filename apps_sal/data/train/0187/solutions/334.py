class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        minOp = currCustomers = profit = maxProfit = i = totalCustomers = 0

        while customers[-1] == 0:
            customers.pop()

        for c in customers:
            i += 1
            currCustomers += c
            totalCustomers += min(4, currCustomers)
            profit = (boardingCost * totalCustomers - (i + 1) * runningCost)
            currCustomers -= min(4, currCustomers)
            if profit > maxProfit:
                maxProfit = profit
                minOp = i
            # print(profit, i, boardingCost, totalCustomers)

        # print(currCustomers, i, profit)
        while currCustomers:
            i += 1
            totalCustomers += min(4, currCustomers)
            profit = (boardingCost * totalCustomers - (i + 1) * runningCost)
            currCustomers -= min(4, currCustomers)
            if profit > maxProfit:
                maxProfit = profit
                minOp = i
            # profit += (boardingCost * currCustomers - (math.factorial(int(ceil(currCustomers/4)))-math.factorial(i)) * runningCost)
            # i += ceil(currCustomers/4)

        return minOp if maxProfit > 0 else -1
