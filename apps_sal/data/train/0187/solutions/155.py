class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        customers_waiting = 0
        max_till_now = 0
        prev_cost = 0
        answer = -1

        for index, customer in enumerate(customers):
            on_board = min(customer + customers_waiting, 4)
            customers_waiting = customer + customers_waiting - 4 if on_board == 4 else 0

            cost = prev_cost + on_board * boardingCost - runningCost
            prev_cost = cost

            if cost > max_till_now:
                max_till_now = cost
                answer = index + 1

        while customers_waiting:
            index += 1
            on_board = min(customers_waiting, 4)
            customers_waiting = customers_waiting - 4 if on_board == 4 else 0

            cost = prev_cost + on_board * boardingCost - runningCost
            prev_cost = cost

            if cost > max_till_now:
                max_till_now = cost
                answer = index + 1

        return answer
