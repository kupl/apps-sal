class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        max_rotation = queue = 0
        people = 0
        i = 0
        rotation = 0
        while i < len(customers) or queue > 0:
            if i < len(customers):
                queue += customers[i]
                i += 1

            if queue == 0:
                rotation += 1
                continue

            board = 4 if queue >= 4 else queue
            queue -= board
            people += board
            rotation += 1

            profit = people * boardingCost - (rotation) * runningCost
            if profit > max_profit:
                max_profit = profit
                max_rotation = rotation

        return max_rotation if profit > -1 else -1
