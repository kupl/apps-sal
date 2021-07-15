class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = [0]
        waiting = 0
        wheel = deque([0] * 4)
        onBoard = 0
        
        for i in range(len(customers)):
            waiting += customers[i]
            new = min(4, waiting)
            waiting -= new
            leaving = wheel.pop()
            onBoard += new - leaving
            wheel.appendleft(new)
            profits.append(profits[-1] + new*boardingCost - runningCost)
        
        while waiting:
            new = min(4, waiting)
            waiting -= new
            leaving = wheel.pop()
            onBoard += new - leaving
            wheel.appendleft(new)
            profits.append(profits[-1] + new*boardingCost - runningCost)
            
        maximum = 0
        index = -1
        for i, val in enumerate(profits):
            if val > maximum:
                maximum = val
                index = i
                
        return index

