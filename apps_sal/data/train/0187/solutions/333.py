class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        i = 0
        waiting = 0
        board = 0
        rot = 0
        res = 0
        ind = -1

        while waiting > 0 or i < n:
            if i < n:
                waiting += customers[i]
            rot += 1
            board += min(4, waiting)
            waiting -= min(4, waiting)
            prof = board * boardingCost - rot * runningCost
            if (prof > res):
                res = prof
                ind = i + 1
            i += 1

        return ind
