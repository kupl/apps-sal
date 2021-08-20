class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (bc, rc, n) = (boardingCost, runningCost, len(customers))
        (res, sum_v, max_v, wait, i) = (-1, 0, 0, 0, 0)
        if 4 * bc <= rc:
            return -1
        while i < n or wait > 0:
            wait += customers[i] if i < n else 0
            cur = wait if wait < 4 else 4
            wait -= cur
            sum_v += cur * bc - rc
            if sum_v > max_v:
                max_v = sum_v
                res = i + 1
            i += 1
        return res
