class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        steps, waiting = 1, 0
        fee, cost, record, max_profit = 0, 0, {}, -sys.maxsize
        while steps < len(customers) or waiting > 0:
            arrival = customers[steps - 1] if steps <= len(customers) else 0
            if arrival + waiting <= 4:
                fee += (arrival + waiting) * boardingCost
                waiting = 0
            else:
                waiting = (arrival + waiting) - 4
                fee += 4 * boardingCost
            cost += runningCost
            record[steps] = fee - cost
            max_profit = max(max_profit, fee - cost)
            steps += 1
        for k in record:
            if record[k] > 0 and record[k] == max_profit:
                return k
        return -1
