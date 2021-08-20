class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best = (0, -1)
        boarded = 0
        cur = rotations = 0
        for customer in customers:
            cur += customer
            boarded += min(cur, 4)
            cur -= min(cur, 4)
            rotations += 1
            cur_revenue = boarded * boardingCost - rotations * runningCost
            if best[0] < cur_revenue:
                best = (cur_revenue, rotations)
        while cur > 0:
            boarded += min(cur, 4)
            cur -= min(cur, 4)
            rotations += 1
            cur_revenue = boarded * boardingCost - rotations * runningCost
            if best[0] < cur_revenue:
                best = (cur_revenue, rotations)
        return best[1]
