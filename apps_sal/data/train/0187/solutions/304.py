class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        best_turns = -1
        customers_waiting = 0
        current_boarded = 0
        current_rotates = 0
        current_index = 0
        while current_index < len(customers) or customers_waiting > 0:
            # print(current_index, customers_waiting)
            # board new customers (at most 4)
            if current_index < len(customers):
                customers_waiting += customers[current_index]

            new_customers = min(4, customers_waiting)
            customers_waiting -= new_customers

            current_boarded += new_customers
            current_rotates += 1
            current_profit = current_boarded * boardingCost - current_rotates * runningCost
            # print(current_profit, current_rotates)

            if current_profit > max_profit:
                max_profit = current_profit
                best_turns = current_rotates

            current_index += 1

        return best_turns
