class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_line = 0
        cur_cus = 0
        cur_rot = 0
        profit = []
        for (i, j) in enumerate(customers):
            cur_line += j
            cur_cus += min(4, cur_line)
            cur_line = max(0, cur_line - 4)
            cur_rot += 1
            profit.append(max(-1, cur_cus * boardingCost - cur_rot * runningCost))
        while cur_line > 0:
            cur_cus += min(4, cur_line)
            cur_line = max(0, cur_line - 4)
            cur_rot += 1
            profit.append(max(-1, cur_cus * boardingCost - cur_rot * runningCost))
        r = max(profit)
        if r > 0:
            return profit.index(r) + 1
        else:
            return -1
