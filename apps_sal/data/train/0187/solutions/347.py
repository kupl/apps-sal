class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        max_spin = -1
        
        cur_profit = 0
        cur_num = 0
        
        spins = 0
        
        for i in range(len(customers)):
            spins += 1
            cur_profit -= runningCost
            
            cur_num += customers[i]
            cur_profit += min(cur_num, 4) * boardingCost

            if cur_profit > max_profit:
                max_profit = max(max_profit, cur_profit)
                max_spin = spins
                
            cur_num = max(0, cur_num - 4)
            
        while cur_num > 0:
            spins += 1
            cur_profit -= runningCost
            cur_profit += min(4, cur_num) * boardingCost
            
            if cur_profit > max_profit:
                max_profit = max(max_profit, cur_profit)
                max_spin = spins
                
            cur_num -= min(4, cur_num)
            
        return max_spin
