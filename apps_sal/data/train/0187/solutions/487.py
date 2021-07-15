class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        it = -1
        max_p = 0
        p = 0
        i = 0
        t = 0
        while i < len(customers) - 1 or customers[-1] > 0:
            cb = min(customers[i], 4)
            if i != len(customers) - 1:                
                customers[i+1] += customers[i] - cb             
                i += 1
            else:
                customers[i] -= cb
            p += cb * boardingCost - runningCost
            t += 1
            if p > max_p:
                max_p = p
                it = t
        return it

