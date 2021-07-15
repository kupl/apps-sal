class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        n = len(customers)
        curr_profit = max_profit = 0
        max_index = 0
        remain = 0
        i = 0
        while i < n or remain > 0:
            if i < n:
                remain += customers[i]
            i += 1
            curr_profit += min(4, remain) * boardingCost - runningCost
            remain = max(0, remain - 4)
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_index = i
        if max_profit == 0:
            return -1
        return max_index
