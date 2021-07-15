class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        profit = 0
        queue = 0
        ans = 0
        for i in range(len(customers)):
            queue += customers[i]
            profit += (min(4, queue) * boardingCost - runningCost)
            if profit > max_profit:
                max_profit = profit
                ans = i + 1
            queue -= min(4, queue)
        if max_profit == -1:
            return -1
        a = (queue * boardingCost) - runningCost * math.ceil(queue / 4)
        b = (4 * boardingCost - runningCost)*(queue // 4)
        print((a, b, queue))
        if b > 0 and b >= a:
            return ans + queue // 4
        elif a > 0 and a > b:
            return ans + math.ceil(queue / 4)
        else:
            return ans

