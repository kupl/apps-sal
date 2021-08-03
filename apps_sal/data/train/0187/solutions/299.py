class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr_ppl_ttl = 0
        profit = list()
        waiting = 0
        line_count = 0
        runtime = 1

        while line_count < len(customers) or waiting != 0:
            if line_count < len(customers):
                if customers[line_count] + waiting > 4:
                    curr_ride = 4
                    waiting = waiting + customers[line_count] - 4
                else:
                    curr_ride = waiting + customers[line_count]
                    waiting = 0
            else:
                if waiting > 4:
                    curr_ride = 4
                    waiting -= curr_ride
                else:
                    curr_ride = waiting
                    waiting = 0
            curr_ppl_ttl += curr_ride
            profit.append(curr_ppl_ttl * boardingCost - runningCost * runtime)
            line_count += 1
            runtime += 1

        if all(i < 0 for i in profit):
            return -1
        return profit.index(max(profit)) + 1
