class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        p = 0
        maxp = 0
        res = -1
        curr = 0
        i = 0
        while curr or i < len(customers):
            if i < len(customers):
                curr += customers[i]
            i += 1
            p += min(curr, 4) * boardingCost - runningCost
            if p > maxp:
                res = i
                maxp = p
            curr = max(0, curr - 4)
        return res
