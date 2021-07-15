class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        capacity = [0] * 4
        waiting = 0
        max_profit = [0,0]
        rot = 0
        j = 0
        i = 0
        l = len(customers)
        cust = 0
        while waiting > 0 or i < l:
            if i < l:
                waiting += customers[i]
                i += 1
            capacity[j] = 0
            capacity[j] = waiting if waiting <= 4 else 4
            cust += capacity[j]
            rot += 1
            waiting = 0 if waiting <= 4 else waiting - 4
            profit = (cust * boardingCost) - (rot * runningCost)
            #print([rot, profit])
            if profit > max_profit[1]:
                max_profit = [rot, profit]
            if j == 3:
                j = 0
            else:
                j += 1
        return max_profit[0] if max_profit[1] > 0 else -1
