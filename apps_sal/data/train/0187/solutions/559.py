class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = times_rotated = float('-inf')
        total_customers = ran = left = i = 0
        while i < len(customers) or left > 0:
            if i < len(customers):
                left += customers[i]
            if i < ran:
                i += 1
                continue
            if left >= 4:
                times = left // 4
                total_customers += 4 * times
                ran += times
                left -= 4 * times
            else:
                total_customers += left
                left = 0
                ran += 1

            curr_profit = total_customers * boardingCost - ran * runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                times_rotated = ran
            i += 1
            # print(total_customers, ran, curr_profit)
        if max_profit < 0:
            return -1
        return times_rotated
