class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        times = 0
        for i in range(len(customers)-1):
            if customers[i] <= 4:
                times +=1
                curr_profit = customers[i]*boardingCost - times*runningCost
            else:
                times +=1
                curr_profit = 4*boardingCost - runningCost
                customers[i+1] = customers[i+1] + customers[i] - 4
            #print(customers)
            profit.append(curr_profit)
        while customers[-1] > 4:
            times +=1
            curr_profit = 4*boardingCost - runningCost
            profit.append(curr_profit)
            customers[-1] -= 4
        times +=1
        curr_profit = customers[-1]*boardingCost - runningCost
        profit.append(curr_profit)
        
        tot_profit = []
        max_profit = 0
        for i in range(len(profit)):
            max_profit += profit[i]
            tot_profit.append(max_profit)
        
        real_max = max(tot_profit)
        
        if real_max < 0:
            return -1
        else:
            return tot_profit.index(real_max)+1

