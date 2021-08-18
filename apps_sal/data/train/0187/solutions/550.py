class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        return self.min_operations_max_profit_recurse(customers, 0, boardingCost, runningCost, 0, 0)[1]

    def serve_remaining_people(self, waiting, boardingCost, runningCost, depth):
        profit = 0

        num_rotations = waiting // 4
        if num_rotations and 4 * boardingCost - runningCost > 0:
            depth += num_rotations
            profit += (4 * boardingCost - runningCost) * num_rotations

        if waiting % 4 and waiting % 4 * boardingCost - runningCost > 0:
            depth += 1
            profit += waiting % 4 * boardingCost - runningCost
        return profit, depth

    def min_operations_max_profit_recurse(self, customers, index, boardingCost, runningCost, waiting, depth):
        if index == len(customers):
            return self.serve_remaining_people(waiting, boardingCost, runningCost, depth)

        waiting += customers[index]
        gondola = min(waiting, 4)
        waiting -= gondola

        profit, rotations = self.min_operations_max_profit_recurse(customers, index + 1, boardingCost, runningCost, waiting, depth + 1)
        profit += gondola * boardingCost - runningCost

        if profit <= 0:
            return -1, -1
        return profit, rotations
