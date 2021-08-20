class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = served = i = 0
        maxProf = -1
        index = -1
        while True:
            if i < len(customers):
                waiting += customers[i]
            boarded = min(4, waiting)
            waiting -= boarded
            served += boarded
            i += 1
            if served * boardingCost - i * runningCost > maxProf:
                maxProf = served * boardingCost - i * runningCost
                index = i
            if waiting == 0 and i > len(customers):
                break
        return index
