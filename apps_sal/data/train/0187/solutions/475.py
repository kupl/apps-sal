class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        r, maxProfit, accProfit, accCustomers,  = -1, 0, 0, 0
        
        i = 0
        while True:
            curr = 0
            if i < len(customers): curr = customers[i]
            accProfit += min(curr + accCustomers, 4)*boardingCost - runningCost
            accCustomers = max(curr + accCustomers - 4, 0)  
            if accProfit > maxProfit:
                r = i + 1
                maxProfit = accProfit
            i += 1
            if i >= len(customers) and accCustomers <= 0: break
        return r
