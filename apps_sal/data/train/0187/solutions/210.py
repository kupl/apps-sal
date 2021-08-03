class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        i = 0
        num_waiting = 0
        ans = -1
        max_profit = 0
        taken = 0
        while i < n or num_waiting:
            curr = num_waiting
            if i < n:
                curr += customers[i]
            if curr > 4:
                taken += 4
                num_waiting = curr - 4
            elif curr > 0:
                taken += curr
                num_waiting = 0
            elif curr == 0:
                num_waiting = 0

            if boardingCost * taken - runningCost * (i + 1) > max_profit:
                max_profit = boardingCost * taken - runningCost * (i + 1)
                ans = i + 1
            i += 1
        return ans
