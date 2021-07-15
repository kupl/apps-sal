class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = [0]
        wait = 0
        for i in customers:
            board = 0
            wait += i
            if wait > 4:
                board = 4
                wait -= 4
            else:
                board = wait
                wait = 0
            profit = board*boardingCost - runningCost
            res.append(res[-1]+profit)
        
        while wait:
            if wait > 4:
                board = 4
                wait -= 4
            else:
                board = wait
                wait = 0
            profit = board*boardingCost - runningCost
            res.append(res[-1]+profit)
        m = max(res)
        if m <= 0:
            return -1
        else:
            return res.index(m)

