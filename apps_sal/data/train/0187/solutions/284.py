class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        customers.reverse()
        curr_boarding_cost = 0
        curr_running_cost = 0
        cnt = 0
        pp = 0
        max_cnt = -1
        while customers or pp:
            if customers:
                pp += customers.pop()
            curr_running_cost += runningCost
            cnt += 1
            pay = min(4, pp)
            curr_boarding_cost += boardingCost * pay
            pp -= pay
            if max_profit < (curr_boarding_cost - curr_running_cost):
                max_cnt = cnt
                max_profit = curr_boarding_cost - curr_running_cost
        return max_cnt
