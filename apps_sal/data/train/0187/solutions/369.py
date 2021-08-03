class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        best_profit = 0
        curr_enqueued = 0
        curr_profit = 0

        def get_customers(i):
            if i >= len(customers):
                return 0
            return customers[i]

        i = 0
        best_turns = -1
        while curr_enqueued > 0 or i < len(customers):
            curr_enqueued += get_customers(i)
            to_add = min(4, curr_enqueued)
            curr_profit += to_add * boardingCost - runningCost
            if curr_profit > best_profit:
                best_turns = i + 1
                best_profit = curr_profit
            curr_enqueued -= to_add
            i += 1
        return best_turns
