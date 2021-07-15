class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        minOp = currCustomers = profit = maxProfit = i = totalCustomers = 0
        
        while i < len(customers) or currCustomers > 0:
            i += 1
            currCustomers += 0 if i > len(customers) else customers[i-1]
            totalCustomers += min(4, currCustomers)
            profit = (boardingCost * totalCustomers - (i+1) * runningCost)
            currCustomers -= min(4, currCustomers)
            if profit > maxProfit:
                maxProfit = profit
                minOp = i
            
        return minOp if maxProfit > 0 else -1

