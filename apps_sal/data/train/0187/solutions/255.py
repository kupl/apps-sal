class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = profit = maxprofit = i = waiting = 0
        while i < len(customers) or waiting:
            if i < len(customers):
                waiting += customers[i]
            waiting -= (boarding := min(waiting, 4))
            if boarding:
                profit += boarding * boardingCost
            profit -= runningCost    
            if profit > maxprofit:
                maxprofit = profit
                ans = i + 1
            i += 1    
        return ans if ans > 0 else -1
