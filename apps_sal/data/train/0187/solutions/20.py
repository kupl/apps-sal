class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        
        max_profit = 0 
        cur_profit = 0
        l = 0
        best_turn = 0
        turn = 1
        for c in customers:
            l += c
            
            if l>4:
                cur_profit += 4*boardingCost - runningCost
                l -= 4
            else:
                cur_profit += l*boardingCost - runningCost
                l = 0
                
            if max_profit < cur_profit:
                max_profit = cur_profit
                best_turn = turn
            turn += 1
        
        while l > 0:
            if l>4:
                cur_profit += 4*boardingCost - runningCost
                l -= 4
            else:
                cur_profit += l*boardingCost - runningCost
                l = 0
                
            if max_profit < cur_profit:
                max_profit = cur_profit
                best_turn = turn
            turn += 1
                
            
        
        
        return -1 if best_turn == 0 else best_turn
