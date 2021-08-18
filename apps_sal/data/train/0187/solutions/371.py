class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        cur = remain = rot = 0
        max_profit = min_rot = -1
        i = 0
        while i < n or remain:
            rot += 1
            remain += customers[i] if i < n else 0
            cur += min(4, remain)
            remain -= min(4, remain)
            cur_profit = cur * boardingCost - rot * runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                min_rot = rot
            i += 1
        return min_rot if max_profit > 0 else -1
