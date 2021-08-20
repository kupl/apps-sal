class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = []
        occupy = 0
        cur_waiting = 0
        k = 0
        while cur_waiting == 0:
            cur_waiting = customers[k]
            k += 1
        m = k
        counter = 0
        while cur_waiting > 0:
            if cur_waiting < 4:
                occupy += cur_waiting
                cur_waiting = 0
            else:
                occupy += 4
                cur_waiting -= 4
            counter += 1
            profits.append(occupy * boardingCost - counter * runningCost)
            if k < len(customers):
                cur_waiting += customers[k]
                k += 1
        z = max(profits)
        if z > 0:
            return profits.index(z) + m
        else:
            return -1
