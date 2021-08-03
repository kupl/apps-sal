class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        pending = 0
        custom = 0
        cur = 0
        res = -1
        i = 0
        while pending or i < n:
            temp = pending + (customers[i] if i < n else 0)
            custom += min(temp, 4)
            profit = custom * boardingCost - (i + 1) * runningCost
            if profit > cur:
                cur = profit
                res = i + 1
            pending = max(0, temp - min(temp, 4))
            i += 1
        return res
