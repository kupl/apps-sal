class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0

        shifts = 0

        waiting_customer = 0
        total_customer = 0

        max_profit = -1
        max_shift = 0

        for customer in customers:
            curr_customer = customer + waiting_customer

            boarding_customer = min(curr_customer, 4)
            waiting_customer = max(0, curr_customer - boarding_customer)

            total_customer += boarding_customer
            shifts += 1

            curr_profit = total_customer * boardingCost - shifts * runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_shift = shifts

        while waiting_customer > 0:
            boarding_customer = min(waiting_customer, 4)
            waiting_customer = max(0, waiting_customer - boarding_customer)

            total_customer += boarding_customer
            shifts += 1
            curr_profit = total_customer * boardingCost - shifts * runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_shift = shifts

        if max_profit <= 0:
            return -1

        return max_shift
