class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost < runningCost:
            return -1
        waiting = 0
        prof = 0
        i = 0
        max_prof, max_i = 0, 0
        while i < len(customers) or waiting > 0:
            if i >= len(customers):
                c = 0
            else:
                c = customers[i]

            boarding = min(waiting + c, 4)
            waiting += c - boarding
            prof += boarding * boardingCost - runningCost
            i += 1

            if prof > max_prof:
                max_prof = prof
                max_i = i
        if max_prof == 0:
            return -1
        return max_i
