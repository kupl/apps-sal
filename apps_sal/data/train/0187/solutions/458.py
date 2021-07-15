class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        ans = 0
        
        profit = 0
        ta, tp = 0, 0
        
        i = 0
        while wait or i < len(customers):
            c = 0 if i >= len(customers) else customers[i]
            wait += c

            profit += (min(4, wait) * boardingCost - runningCost)
            ans += 1
            wait = max(0, wait - 4)
            
            # print(profit, ans)
            if profit > tp:
                ta = ans
                tp = profit
                
            i += 1

            
        ans = ta
        profit += (min(4, wait) * boardingCost - runningCost)
        
        
        if profit > tp:
            ans += 1

        return -1 if ans == 0 else ans

