class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waitingCustomers = customers[0]
        totalCustomers = 0
        i = 1
        result = -1
        maxProfit = 0
        
        while i < len(customers) or waitingCustomers > 0:
            servedCustomers = min(4, waitingCustomers)
            
            waitingCustomers -= servedCustomers
            totalCustomers += servedCustomers
            
            profit = totalCustomers * boardingCost - i * runningCost
            if profit > maxProfit:
                maxProfit = profit
                result = i
            
            if i < len(customers):
                waitingCustomers += customers[i]
            
            i += 1
        
        return result

