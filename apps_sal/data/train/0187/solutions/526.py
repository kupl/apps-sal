class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = [-1]
        waiting = customers[0]
        i = 1
        board = 0
        while waiting > 0 or i < len(customers):

            board += min(4, waiting)
            profit = board * boardingCost
            profit -= runningCost * i
            profits.append(profit)
            waiting -= min(4, waiting)
            if i < len(customers):
                waiting += customers[i]

            i += 1

        id = profits.index(max(profits))
        if id == 0:
            return -1

        return id
