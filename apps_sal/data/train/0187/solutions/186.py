class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        profit = 0
        max_profit = float('-inf')
        wc = customers[0]
        i = 1
        rot = 1
        max_rot = 0

        while wc > 0 or i < len(customers):

            if wc >= 4:
                # print wc
                wc -= 4
                profit += 4 * boardingCost
            elif wc < 4:
                bc = wc
                wc = 0
                profit += bc * boardingCost
            profit -= runningCost
            prev = max_profit
            max_profit = max(profit, max_profit)
            if max_profit != prev:
                max_rot = rot
            if i < len(customers):
                wc += customers[i]
                i += 1

            rot += 1

        if max_profit > 0:
            return max_rot
        else:
            return -1
