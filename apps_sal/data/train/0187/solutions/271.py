class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        bal = 0
        max_bal = 0
        max_rot = -1
        rot = 0
        for c in customers:
            rot += 1
            waiting += c
            bal += min(4, waiting) * boardingCost - runningCost
            if bal > max_bal:
                max_rot = rot
                max_bal = bal
            waiting -= min(4, waiting)
        
        while waiting:
            rot += 1
            bal += min(4, waiting) * boardingCost - runningCost
            if bal > max_bal:
                max_rot = rot
                max_bal = bal
            waiting -= min(4, waiting)
        
        return max_rot

