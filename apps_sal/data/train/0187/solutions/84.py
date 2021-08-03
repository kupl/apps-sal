class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        count = 0
        current = 0
        res = 0
        rolls = 0
        for i in range(len(customers)):
            count += customers[i]
            temp = min(4, count)
            count -= temp
            current += boardingCost * temp
            current -= runningCost
            if current > res:
                res = current
                rolls = i + 1
        current += boardingCost * (count // 4 * 4)
        current -= runningCost * (count // 4)
        if current > res:
            res = current
            rolls = len(customers) + count // 4
        current += boardingCost * (count % 4)
        current -= runningCost
        if current > res:
            res = current
            rolls = len(customers) + count // 4 + 1
        if res == 0:
            return -1
        return rolls
