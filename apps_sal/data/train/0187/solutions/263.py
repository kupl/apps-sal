class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        maximum = 0
        lastProfit = 0
        waiting = 0
        wheel = deque([0] * 4)
        onBoard = 0
        count = 0
        
        for i in range(len(customers)):
            waiting += customers[i]
            new = min(4, waiting)
            waiting -= new
            leaving = wheel.pop()
            onBoard += new - leaving
            wheel.appendleft(new)
            count += 1
            profit = lastProfit + new*boardingCost - runningCost
            if maximum < profit:
                maximum = profit
                res = count
            lastProfit = profit
        
        while waiting:
            new = min(4, waiting)
            waiting -= new
            leaving = wheel.pop()
            onBoard += new - leaving
            wheel.appendleft(new)
            count += 1
            profit = lastProfit + new*boardingCost - runningCost
            if maximum < profit:
                maximum = profit
                res = count
            lastProfit = profit
            
        return res

