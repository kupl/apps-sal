class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n, cur, i = len(customers), 0, 0
        maxProfit, maxProfitIdx, curProfit = 0, -1, 0
        while i < n or cur > 0:
            cur += customers[i] if i < n else 0            
            i += 1
            
            board = min(cur, 4)
            cur -= board
            
            curProfit += board * boardingCost - runningCost
            if curProfit > maxProfit:
                maxProfit, maxProfitIdx = curProfit, i     
        
        return maxProfitIdx if maxProfit > 0 else -1 
