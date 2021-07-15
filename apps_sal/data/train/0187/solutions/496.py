class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        
        i = 0
        r = 0
        profit = 0
        max_p = float('-inf')
        ans = -1
        while i < len(customers) or left > 0:
            if i < len(customers):
                left += customers[i]
            
            board = min(4, left)
            left = max(0, left - 4)
            r += 1
            profit += boardingCost*board - runningCost
            if profit > 0 and profit > max_p:
                max_p = profit
                ans = r
                
            i += 1
            
        return ans
            
            
            
            
            
            
        

