class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        i = 0
        n = len(customers)
        max_profit, min_rotates = 0, -1
        total_boarded = 0

        rotate = 0
        while True:
            if i == n and not wait:
                break

            if i < n:
                wait += customers[i]
                i += 1

            rotate += 1

            board = min(wait, 4)
            wait -= board
            total_boarded += board

            profit = total_boarded * boardingCost - rotate * runningCost

            if profit > max_profit:
                max_profit = profit
                min_rotates = rotate

        return min_rotates
