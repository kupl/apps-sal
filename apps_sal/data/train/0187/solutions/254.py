class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = 0
        res = (-1, 0)
        waiting = 0
        boarded = 0
        i = 0
        while i < len(customers) or waiting != 0:
            if i < len(customers):
                waiting += customers[i]
            if waiting >= 4:
                waiting -= 4
                boarded += 4
            else:
                boarded += waiting
                waiting = 0
            ans = boarded * boardingCost - (i + 1) * runningCost
            if ans > res[1]:
                res = (i + 1, ans)
            i += 1
        return res[0]
