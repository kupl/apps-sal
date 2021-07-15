class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        num_wait = 0
        num_board = 0
        num_round = 0
        max_prof = 0
        res = -1
        for a in customers:
            num_round += 1
            if num_wait + a >= 4:
                num_board += 4
                num_wait += a - 4
            else:
                num_board += num_wait + a
                num_wait = 0
            if boardingCost * num_board - runningCost * num_round > max_prof:
                max_prof = max(max_prof, boardingCost * num_board - runningCost * num_round)
                res = num_round
            
        while num_wait > 0:
            num_round += 1
            num_board += min(4, num_wait)
            num_wait -= min(4, num_wait)
            if boardingCost * num_board - runningCost * num_round > max_prof:
                max_prof = max(max_prof, boardingCost * num_board - runningCost * num_round)
                res = num_round 
        return res
            

