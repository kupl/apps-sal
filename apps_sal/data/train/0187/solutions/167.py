class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        rotations = 0
        profit, max_profit = 0, 0
        res = -1

        def xreport(boarded: int):
            nonlocal profit, rotations, max_profit, res
            profit += boarded * boardingCost - runningCost
            rotations += 1
            if profit > max_profit:
                max_profit = profit
                res = rotations
            return

        for i in range(len(customers) - 1):
            if customers[i] > 4:
                customers[i + 1] += customers[i] - 4
                customers[i] = 4

            xreport(customers[i])

        waiting = customers[-1]
        while waiting > 0:
            if waiting > 4:
                waiting -= 4
                xreport(4)
            else:
                xreport(waiting)
                waiting = 0

        return res
