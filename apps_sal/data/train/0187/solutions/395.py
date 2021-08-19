class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        count = 0
        profit = 0
        rem = 0
        onBoard = 0
        max_profit_rounds = -1
        max_profit = 0
        while True:
            if i >= len(customers) - 1 and rem == 0:
                break
            if i < len(customers):
                rem += customers[i]
                i += 1
            count += 1
            if rem > 4:
                onBoard += 4
                rem -= 4
            else:
                onBoard += rem
                rem = 0
            profit = onBoard * boardingCost - count * runningCost
            if profit > max_profit:
                max_profit = profit
                max_profit_rounds = count
        if max_profit < 0:
            return -1
        return max_profit_rounds
