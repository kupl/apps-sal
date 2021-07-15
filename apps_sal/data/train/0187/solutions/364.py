def getindex(arr):
    value = max(arr)
    cnt = 1
    for e in arr:
        if e == value:
            return cnt
        cnt += 1

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        boarding = 0 
        rotation = 0
        profit = []
        n_customers = len(customers)
        for i in range(n_customers-1):
            if customers[i]<4:
                boarding += customers[i]
                rotation += 1
                profit.append(boarding * boardingCost - rotation*runningCost)
            else:
                boarding += 4
                customers[i+1] = customers[i] + customers[i+1] -4
                rotation += 1
                profit.append(boarding * boardingCost - rotation*runningCost)
        while customers[n_customers-1]>3:
            boarding += 4
            rotation += 1
            profit.append(boarding * boardingCost - rotation*runningCost)
            customers[n_customers-1] -= 4
        if customers[n_customers-1] == 0:
            pass
        else:
            boarding += customers[n_customers-1]
            rotation += 1
            profit.append(boarding * boardingCost - rotation*runningCost)
        if max(profit)<0:
            return -1
        else:
            return getindex(profit)

