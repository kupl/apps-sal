import math
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best = 0
        index = None
        i = 0
        n = 0
        p = 0
        while n > 0 or i < len(customers):
            if i < len(customers):
                n += customers[i]
            p += min(4, n) * boardingCost
            p -= runningCost
            n -= min(4, n)
            i += 1
            if p > best:
                best = p
                index = i
        
        if index is None:
            return -1
        return index
