class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total = wait = ops = ma = 0
        res = -1
        while ops < len(customers) or wait > 0:
            arrival = customers[ops] if ops < len(customers) else 0
            ops += 1
            total += min(4, arrival + wait)
            wait = max(wait + arrival - 4 , 0)
            profit = total * boardingCost - ops * runningCost
            if profit > ma:
                ma = profit
                res = ops
        return res
