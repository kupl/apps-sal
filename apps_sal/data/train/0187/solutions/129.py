class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        max_profit = float('-inf')
        queue = 0
        idx = 0
        min_idx = 0
        profit = 0
        itr = 0

        while True:
            if idx < len(customers):
                queue += customers[idx]
            served = 0
            if queue >= 4:
                queue -= 4
                served = 4
            else:
                served = queue
                queue = 0

            profit += boardingCost * served
            profit -= runningCost
            itr += 1
            #print(f'profit={profit} itr={itr} served = {served} profit = {profit}')
            if profit > max_profit:
                max_profit = profit
                min_idx = itr

            idx += 1
            if queue <= 0 and idx >= len(customers):
                break

        if max_profit <= 0:
            return -1
        else:
            return min_idx
