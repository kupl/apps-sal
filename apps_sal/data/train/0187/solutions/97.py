class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        board = 0
        wait = 0
        profit = 0
        maxProfit = 0
        shift = 0
        time = 0
    
        i, n = 0, len(customers)
        while i < n or wait != 0:
            if i < n:
                customer = customers[i]
                i += 1
            else:
                customer = 0
            wait += customer
            if wait > 4:
                board = 4
                wait -= 4
            else:
                board = wait
                wait = 0
            shift += 1
            profit += board * boardingCost - runningCost
            if profit > maxProfit:
                maxProfit = profit
                time = shift
        return time if maxProfit > 0 else -1

