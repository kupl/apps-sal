class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        cost = 0
        step = 0

        def ceildiv(a, b):
            return -(-a // b)
        for i in range(len(customers)):
            left += customers[i]
            if left >= 4:
                left -= 4
                cost = 4 * (boardingCost) - runningCost
                step += 1

            else:
                cost = left * boardingCost - runningCost
                step += 1
                left = 0
        lefts = left // 4
        leftc = left % 4
        costl = leftc * boardingCost - runningCost
        cost = cost + left * boardingCost - runningCost * lefts
        step += lefts

        if cost > 0:
            if costl > 0:
                return step + 1
            else:
                return step
        else:
            return -1
