class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        backlog = customers[0]
        rotations = 0
        maxprofit = 0

        i = 1
        profit = 0
        # print(profit)
        while backlog > 0 or i < len(customers):
            # print(backlog)
            rotations += 1

            profit += min(4, backlog) * boardingCost - runningCost
            # print(profit)
            if profit > maxprofit:
                maxprofit = profit
                minrounds = rotations

            backlog = backlog - 4 if backlog > 4 else 0
            backlog += customers[i] if i < len(customers) else 0
            i += 1

        if maxprofit > 0:
            return minrounds
        else:
            return -1
