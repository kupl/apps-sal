class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        if not customers:
            return -1
        profits = []
        wait = 0
        i = 0

        while True:
            if i > len(customers) - 1 and wait <= 0:
                break
            elif i <= len(customers) - 1:
                wait += customers[i]
                profit = min(4, wait) * boardingCost - runningCost
                profits.append(profit)
                wait = wait - min(4, wait)
                i += 1
            else:
                profit = min(4, wait) * boardingCost - runningCost
                profits.append(profit)
                wait = wait - min(4, wait)

        # print(profits)

        sum_ = profits[0]
        for i in range(1, len(profits)):
            profits[i] = sum_ + profits[i]
            sum_ = profits[i]

        # print(profits)
        max_ = 0
        index = -1
        for i in range(0, len(profits)):
            if max_ < profits[i]:
                index = i
                max_ = profits[i]

        if index > -1:
            index += 1
        return index
