class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        prev = 0
        total = 0
        maxCost = 0
        for ind in range(len(customers)):
            cur = min(customers[ind] + prev, 4)
            if customers[ind] < 4:
                prev = max(prev - (4 - customers[ind]), 0)

            total += cur
            curCost = total * boardingCost - (ind + 1) * runningCost
            if (curCost > maxCost):
                res = ind + 1
                maxCost = curCost

            if customers[ind] > 4:
                prev += customers[ind] - 4

        ind = len(customers)
        while prev:
            total += min(prev, 4)
            prev = max(prev - 4, 0)
            curCost = total * boardingCost - (ind + 1) * runningCost
            if (curCost > maxCost):
                res = ind + 1
                maxCost = curCost
            ind += 1
        return res
