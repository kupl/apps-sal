class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cust, p, max_p = 0, (0, 0), (float('-inf'), 0)
        idx = 0
        while idx < len(customers) or cust > 0:
            if idx < len(customers):
                cust += customers[idx]
                idx += 1
            p = (p[0] + min(4, cust) * boardingCost - runningCost, p[1] + 1)
            cust -= min(4, cust)
            if p[0] > max_p[0]:
                max_p = p
        return -1 if max_p[0] <= 0 else max_p[1]
