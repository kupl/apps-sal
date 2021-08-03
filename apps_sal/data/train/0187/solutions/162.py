MIN = float('-inf')


class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):

        n = len(customers)
        step, maxStep, maxProfit = 0, 0, MIN
        i, people, queue = 0, 0, 0
        while True:
            if i < n:
                queue += customers[i]
                i += 1
            p = min(4, queue)
            queue -= p
            people += p
            step += 1
            profit = people * boardingCost - step * runningCost
            if profit > maxProfit:
                maxProfit = profit
                maxStep = step
            if queue == 0 and i == n:
                break
        return maxStep if maxProfit > 0 else -1
