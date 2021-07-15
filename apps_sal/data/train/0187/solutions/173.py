class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers or len(customers) == 0:
            return -1
        
        cur_round = 1
        max_round = -1 
        customer_cnt = board_cnt = cur_profit = max_profit = i = 0
        
        while (customer_cnt > 0 or i < len(customers)):
            if i < len(customers):
                customer_cnt += customers[i]
                i += 1
    
            board_cnt = min(customer_cnt, 4)
            customer_cnt -= board_cnt
            
            cur_profit += (board_cnt * boardingCost) - runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_round = cur_round 
            
            cur_round += 1 
        
        return max_round
            
            

