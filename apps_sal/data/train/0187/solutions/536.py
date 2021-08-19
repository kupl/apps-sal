class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting_customers = 0
        wheel_rotations = 0
        minimum_wheel_rotations = -1
        max_profit = 0
        profit = 0
        for c in customers:
            wheel_rotations += 1
            boarding_waiting = min(4, waiting_customers)
            waiting_customers -= boarding_waiting
            boarding_now = max(0, min(4, c) - boarding_waiting)
            waiting_customers += c - boarding_now
            total_boarding = boarding_waiting + boarding_now
            profit += total_boarding * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                minimum_wheel_rotations = wheel_rotations
        fullrevenue_rotations = (waiting_customers // 4)
        wheel_rotations += fullrevenue_rotations
        # fullprofit = fullprofit_rotations * 4 * boardingCost - fullprofit_rotations * runningCost
        fullrevenue = fullrevenue_rotations * (4 * boardingCost - runningCost)

        profit += fullrevenue

        if profit > max_profit:
            max_profit = profit
            minimum_wheel_rotations = wheel_rotations

        remaining_customers = waiting_customers % 4
        wheel_rotations += 1
        remaining_revenue = remaining_customers * boardingCost - runningCost

        profit += remaining_revenue
        if profit > max_profit:
            max_profit = profit
            minimum_wheel_rotations = wheel_rotations
        return minimum_wheel_rotations
