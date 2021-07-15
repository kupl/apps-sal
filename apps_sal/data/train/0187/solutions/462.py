class Solution:
    def minOperationsMaxProfit(self, customers: List[int], board: int, run: int) -> int:
        max_prof = -float('inf')
        profit = 0
        ci = 0
        it = 0
        waiting = 0
        res = 0
        
        while waiting > 0 or ci < len(customers):
            if ci < len(customers):
                waiting += customers[ci]
            
            profit += min(4, waiting) * board
            profit -= run
            if profit > max_prof:
                max_prof = profit
                res = it
            waiting = max(waiting-4, 0)
            ci += 1
            it += 1
            
        
        return res+1 if max_prof > 0 else -1
            

