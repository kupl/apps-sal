class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        i = max = profit = waiting = 0 
        while i < len(customers) or waiting: 
            if i < len(customers): waiting += customers[i]
            board = min(4, waiting)
            waiting -= board 
            profit += board * boardingCost - runningCost 
            if max < profit: 
                ans = i+1
                max = profit
            i += 1
        return ans 
