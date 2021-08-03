class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost or not customers:
            return -1
        profit, res, customer, idx, cnt = 0, 0, 0, 0, 0
        while idx < len(customers) or customer > 0:
            if idx < len(customers):
                customer += customers[idx]
            idx, cnt = idx + 1, cnt + 1
            tmp = profit + boardingCost * min(4, customer) - runningCost
            if tmp > profit:
                res = cnt
            customer = max(0, customer - 4)
            profit = tmp
        return res
