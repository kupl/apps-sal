class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """ greedy.
            only consider boarding, no need to consider get down
        """
        profit = 0
        waited = 0
        rotate = 0
        for c in customers:
            if c + waited >= 4:
                profit += 4 * boardingCost
            else:
                profit += (c + waited) * boardingCost
            waited = max(0, c + waited - 4)
            profit -= runningCost
            rotate += 1
        if waited > 0:
            rotate += waited // 4
            profit += 4 * rotate * boardingCost
            profit -= rotate * runningCost
            if waited % 4 > 0:
                profit += waited % 4 * boardingCost
                profit -= runningCost
                if waited % 4 * boardingCost > runningCost:
                    rotate += 1
        return rotate if profit > 0 else -1
