from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        index, max_profit, waiting_customers, num_customers, best_rotation = 0, -1, 0, 0, -1

        while index < len(customers) or waiting_customers > 0:
            current_num_customers = 0
            rotations = index + 1
            if index < len(customers):
                current_num_customers = customers[index]
            if current_num_customers >= 4:
                waiting_customers += (current_num_customers - 4)
                num_customers += 4
                if num_customers * boardingCost - rotations * runningCost > max_profit:
                    max_profit = num_customers * boardingCost - rotations * runningCost
                    best_rotation = rotations
            elif current_num_customers < 4 and (current_num_customers + waiting_customers) > 4:
                waiting_customers -= (4 - current_num_customers)
                num_customers += 4
                if num_customers * boardingCost - rotations * runningCost > max_profit:
                    max_profit = num_customers * boardingCost - rotations * runningCost
                    best_rotation = rotations
            else:
                num_customers += current_num_customers
                num_customers += waiting_customers
                waiting_customers = 0
                if num_customers * boardingCost - rotations * runningCost > max_profit:
                    max_profit = num_customers * boardingCost - rotations * runningCost
                    best_rotation = rotations
            index += 1

        return best_rotation
