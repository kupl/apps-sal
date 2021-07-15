import math

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx = 0
        ans = -1
        profit = 0
        waiting = 0
        i = 0
        while i<len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
            profit -= runningCost
            if waiting > 4:
                profit += (4 * boardingCost)    
                waiting -= 4
            else:
                profit += (waiting * boardingCost)
                waiting = 0
            if profit > maxx:
                ans = i
                maxx = profit
            i += 1
            # print(f\"profit: {profit}, waiting: {waiting}\")
                
        return ans+1 if ans>-1 else -1
        
        
#         tot = sum(customers)
#         if boardingCost*4 <= runningCost:
#             return -1
        
#         ans = tot // 4
        
#         left = tot % 4
        
#         if left*boardingCost > runningCost:
#             return ans + 1
#         return ans

