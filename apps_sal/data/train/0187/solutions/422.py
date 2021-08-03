class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = []
        profit = 0
        prev = 0
        i = 0
        while i < len(customers):
            curr = customers[i] + prev
            if curr <= 4:
                profit += curr * boardingCost - runningCost
                profits.append(profit)
                prev = 0
            else:
                prev = curr - 4
                profit += 4 * boardingCost - runningCost
                profits.append(profit)
            i += 1
            if i == len(customers) and prev != 0:
                i -= 1
                customers[i] = 0
        if max(profits) < 0:
            return -1
        m = 0
        ind = 0
        for i in range(len(profits)):
            if profits[i] > m:
                m = profits[i]
                ind = i
        return ind + 1
