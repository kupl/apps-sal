class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        user = 0
        profit = 0
        ind = 0
        i = 0
        while ind < len(customers) or user > 0:
            if ind < len(customers):
                x = customers[ind]
                user += x
            ind += 1
            profit += min(user,4)*boardingCost - runningCost
            if res < profit:
                res = profit
                i = ind
            user -= min(user,4)
        return i if res > 0 else -1

