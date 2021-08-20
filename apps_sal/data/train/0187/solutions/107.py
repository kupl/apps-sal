class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (mx, ans) = (-1, -1)
        (wait, income, cost) = (0, 0, 0)
        for i in range(1, 51 * 100000):
            if i <= len(customers):
                wait += customers[i - 1]
            elif wait == 0:
                break
            if wait >= 4:
                onboard = 4
            else:
                onboard = wait
            wait -= onboard
            income += onboard * boardingCost
            cost += runningCost
            curr = income - cost
            if curr > mx:
                mx = curr
                ans = i
        return ans
