class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        if boardingCost * 4 <= runningCost:
            return -1
        
        profit = 0
        num_waiting_customers = 0
        max_profit = 0
        ans = -1
        
        i = 0
        
        while i < len(customers) or num_waiting_customers > 0:
            num_waiting_customers += customers[i] if i < len(customers) else 0
            
            # if i < len(customers):
            #     num_rotate = ((len(customers) - i) * 50 + num_waiting_customers + 3) // 4
            #     if ((len(customers) - i) * 50 + num_waiting_customers) * boardingCost - num_rotate * runningCost + profit < 0:
            #         return ans
                    
            
            profit += min(num_waiting_customers, 4) * boardingCost - runningCost
            
            if profit > max_profit:
                ans = i + 1
                max_profit = profit
            
            num_waiting_customers = max(num_waiting_customers - 4, 0)
            i += 1
        return ans

