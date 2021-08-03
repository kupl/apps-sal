class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        maxProf = 0
        profit = wait = ground = 0
        on = [0, 0, 0, 0]
        index = 0
        while (index < len(customers)) or (wait != 0):
            c = 0 if index >= len(customers) else customers[index]
            on[ground] = min(4, c + wait)
            wait = wait + c - on[ground]
            diff = on[ground] * boardingCost - runningCost
            profit += diff
            index += 1
            if profit > maxProf:
                maxProf = profit
                ans = index
            ground = (ground + 1) % 4
        return ans
