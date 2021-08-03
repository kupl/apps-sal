class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost < runningCost or len(customers) == 0:
            return -1

        maxVal = 0
        times, recordedTime = 0, 0
        served, waitting = 0, 0
        while times < len(customers) or waitting != 0:
            if times < len(customers):
                waitting = waitting + customers[times]

            if waitting > 4:
                served += 4
                waitting -= 4
            else:
                served += waitting
                waitting = 0

            times += 1
            currentProfit = served * boardingCost - times * runningCost
            if currentProfit > maxVal:
                maxVal = currentProfit
                recordedTime = times

        return recordedTime if recordedTime > 0 else -1
