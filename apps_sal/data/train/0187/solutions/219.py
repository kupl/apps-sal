class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int,
                               runningCost: int) -> int:
        gondolas = [0] * 4
        curr_gondola = 0
        n = len(customers)
        max_profit = profit = 0
        min_rotation = 0
        rotations = 0
        waiting = 0
        i = 0
        while i < n or waiting:
            if i < n:
                while customers[i] < 4 and waiting:
                    customers[i] += 1
                    waiting -= 1
            if i < n:
                customer = customers[i]
                if customer > 4:
                    waiting += customer - 4
                    customer = 4
                curr_gondola = (1 + curr_gondola) % 4
                profit += customer * boardingCost
            else:
                customer = min(4, waiting)
                waiting -= customer
                profit += customer * boardingCost
            profit -= runningCost
            rotations += 1
            if profit > max_profit:
                min_rotation = rotations
                max_profit = profit
            if i < n:
                i += 1

        print((max_profit, rotations, min_rotation, customers))
        if max_profit <= 0:
            return -1
        return min_rotation
