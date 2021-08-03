class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        times = 0
        left = 0
        profit = 0
        pros = []
        for i in range(len(customers)):
            left += customers[i]
            profit = profit + min(left, 4) * boardingCost - runningCost
            pros.append(profit)
            left = max(0, left - 4)
            times += 1
        i = len(customers)
        while (left > 0):
            profit = profit + min(left, 4) * boardingCost - runningCost
            pros.append(profit)
            i += 1
            left = max(0, left - 4)
            times += 1
        mm = -1
        out = - 1
        for i in range(len(pros)):
            if pros[i] > mm:
                mm = pros[i]
                out = i + 1
        if profit > 0:
            return out
        return -1
