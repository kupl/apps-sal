class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4:
            return -1
        max_p = 0
        max_idx = 0
        cur_p = 0
        turn = 0
        wait = 0
        for c in customers:
            c += wait
            cur_p += boardingCost * max(4, c) - runningCost
            turn += 1
            if cur_p > max_p:
                max_idx = turn
                max_p = cur_p
            wait = c - min(c, 4)
        if wait == 0:
            return max_idx
        print((turn, wait))
        cur_p += boardingCost * (wait - wait % 4) - int(wait / 4) * runningCost
        if cur_p > max_p:
            max_p = cur_p
            max_idx = turn + int(wait / 4)
        cur_p += wait % 4 * boardingCost - runningCost
        if cur_p > max_p:
            max_idx = turn + int(wait / 4) + 1
        return max_idx
