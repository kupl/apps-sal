class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit, res, remain, profit, i = 0, 0, 0, -runningCost*3, 0
        while i < len(customers) or remain:
            if i < len(customers):
                x = customers[i]
            else:
                x = 0
            
            profit += min(4, x + remain) * boardingCost - runningCost
            
            if profit > maxProfit:
                maxProfit, res = profit, i+1
            remain = max(0, remain+x-4)
            i += 1
        return res if res else -1
