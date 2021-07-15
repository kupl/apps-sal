class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        prof = 0; max_prof = 0; max_run = 0; run = 0; i = 0
        waiting = 0
        
        while waiting > 0 or i < len(customers):
            if i < len(customers): 
                waiting += customers[i]
                i += 1
            board = min(4, waiting)
            waiting -= board
            prof += boardingCost * board - runningCost
            run += 1
            if prof > max_prof:
                max_prof = prof
                max_run = run
        return max_run if max_prof != 0 else -1
