class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        rnd = 0
        income = 0
        cost = 0
        profit = []
        while waiting > 0 or rnd < len(customers):
            if rnd < len(customers):
                waiting += customers[rnd]
            ride = min(4, waiting)
            income += ride * boardingCost
            waiting -= ride
            cost += runningCost
            profit.append(income - cost)
            rnd += 1
        if max(profit) > 0:
            return profit.index(max(profit)) + 1
        return -1
