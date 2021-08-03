class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost - runningCost < 0:
            return -1
        n = len(customers)
        prof, max_prof = 0, -1000
        rot, min_rot = 0, 0
        c_sum = 0
        for i, c in enumerate(customers):
            c_sum += c
            if c_sum >= 4:
                prof += 4 * boardingCost - runningCost
                c_sum -= 4
            else:
                prof += c_sum * boardingCost - runningCost
                c_sum = 0
            if prof > max_prof:
                max_prof = prof
                min_rot = i + 1
        flag = (c_sum % 4) * boardingCost - runningCost > 0
        prof += c_sum * boardingCost - (c_sum // 4 + flag) * runningCost
        if prof > max_prof:
            max_prof = prof
            min_rot = n + c_sum // 4 + flag

        return min_rot if max_prof > 0 else -1
