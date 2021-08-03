class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        if 4 * boardingCost - runningCost < 0:
            return -1

        res = []
        total = 0
        for i in range(len(customers) - 1):
            if customers[i] > 4:
                customers[i + 1] += customers[i] - 4
                customers[i] = 4
            total += boardingCost * customers[i] - runningCost
            res.append(total)

        val = customers[len(customers) - 1]
        while(val > 0):
            if val > 4:
                val -= 4
                total += boardingCost * 4 - runningCost
                res.append(total)
            else:
                total += boardingCost * val - runningCost
                res.append(total)
                val = 0
        return res.index(max(res)) + 1
