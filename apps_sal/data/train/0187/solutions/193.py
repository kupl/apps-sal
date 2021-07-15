class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        most = profit = waiting = 0
        for i, x in enumerate(customers): 
            waiting += x # more people waiting in line 
            waiting -= (running := min(4, waiting)) # boarding 
            profit += running * boardingCost - runningCost 
            if most < profit: 
                ans, most = i+1, profit
        q, r = divmod(waiting, 4)
        if 4*boardingCost > runningCost: 
            ans += q
        if r*boardingCost > runningCost: 
            ans += 1
        return ans 
