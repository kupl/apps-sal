class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost :
            return -1
        
        best = 0
        res = -1
        wait = 0
        profit = 0
        rotation = 0
        for customer in customers :
            wait += customer
            rotation += 1
            if wait > 4 :
                wait -= 4
                profit += 4 * boardingCost - runningCost
            else :
                profit += wait * boardingCost - runningCost
                wait = 0
            if profit > best :
                best = profit
                res = rotation
        while wait > 0 :
            rotation += 1
            if wait > 4 :
                wait -= 4
                profit += 4 * boardingCost - runningCost
            else :
                profit += wait * boardingCost - runningCost
                wait = 0
            if profit > best :
                best = profit
                res = rotation
        return res
