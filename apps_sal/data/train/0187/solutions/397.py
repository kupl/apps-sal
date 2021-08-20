class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return -1
        if 4 * boardingCost <= runningCost:
            return -1
        num = 0
        profit = 0
        cur_w = 0
        for i in range(len(customers)):
            num += 1
            cur_w += customers[i]
            n = 4 if cur_w >= 4 else cur_w
            profit += n * boardingCost - runningCost
            cur_w -= n
        (rotates, left) = (cur_w // 4, cur_w % 4)
        num += rotates
        profit += rotates * 4 * boardingCost - runningCost * rotates
        if left * boardingCost > runningCost:
            num += 1
            profit += left * boardingCost - runningCost
        if profit <= 0:
            return -1
        return num
