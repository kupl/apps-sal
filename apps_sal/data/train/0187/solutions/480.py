class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        d = {}
        p = 0
        i = 0
        m = sum(customers) // 4 + 1
        z = customers.count(0)
        for i in range(m + z):
            if customers[i] > 4:
                customers += (0,)
            p += boardingCost * min(customers[i], 4) - runningCost
            if p not in list(d.keys()):
                d[p] = i
            customers[i + 1] += max(customers[i] - 4, 0)
        if max(d) < 0:
            return -1
        return d[max(d)] + 1
