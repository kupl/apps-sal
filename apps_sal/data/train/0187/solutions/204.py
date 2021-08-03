class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotate = 0
        total = 0
        left = 0
        for i in customers:
            total += i
            left += i
            if left <= 4:
                rotate += 1
                left = 0
            left -= 4
            rotate += 1
        rotate += left // 4
        if left % 4 * boardingCost > runningCost:
            rotate += 1
        if boardingCost * total - rotate * runningCost > 0:
            return rotate
        return -1
