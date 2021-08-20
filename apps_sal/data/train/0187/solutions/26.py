class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        local_max = 0
        final_times = 0
        times = 0
        wait_line = 0
        for i in range(len(customers)):
            wait_line += customers[i]
            if wait_line >= 4:
                wait_line -= 4
                res += 4 * boardingCost - runningCost
            elif wait_line < 4:
                res += wait_line * boardingCost - runningCost
                wait_line = 0
            times += 1
            if res > local_max:
                local_max = res
                final_times = times
        while wait_line > 0:
            if wait_line >= 4:
                wait_line -= 4
                res += 4 * boardingCost - runningCost
            elif wait_line < 4:
                res += wait_line * boardingCost - runningCost
                wait_line = 0
            times += 1
            if res > local_max:
                local_max = res
                final_times = times
        if local_max == 0:
            return -1
        else:
            return final_times
