import math
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        len_rot = len(customers)
        if(4*boardingCost <= runningCost or len_rot == 0):
            return -1
        tot = 0
        profit = 0
        lis = []
        for i in customers:
            tot += i
            profit += min(4, tot)*boardingCost - runningCost
            tot -= min(4, tot)
            lis.append(profit)
        while(tot > 0):
            profit += min(4, tot)*(boardingCost) - runningCost
            tot -= min(4, tot)
            lis.append(profit)
        max_value = max(lis)
        return lis.index(max_value)+1 if max_value > 0 else -1

