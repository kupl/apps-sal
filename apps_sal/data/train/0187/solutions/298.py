from typing import *


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        served = 0
        profits = []

        for i, v in enumerate(customers):
            waiting += v
            if waiting < 4:
                served += v
            else:
                served += 4

            profits.append(served * boardingCost - (i + 1) * runningCost)
            if waiting < 4:
                waiting = 0
            else:
                waiting -= 4

        while waiting != 0:
            i += 1
            if waiting < 4:
                served += waiting
            else:
                served += 4

            profits.append(served * boardingCost - (i + 1) * runningCost)

            if waiting < 4:
                waiting = 0
            else:
                waiting -= 4

        index = max(list(range(len(profits))), key=lambda i: profits[i])
        if profits[index] < 0:
            return -1
        else:
            return index + 1
