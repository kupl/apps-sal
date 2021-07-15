class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        maxProfit = 0
        curProfit = 0
        curCustomers = 0
        rounds = 0
        for c in customers:
            rounds += 1
            curCustomers += c
            if curCustomers>=4:
                curProfit += 4 * boardingCost - runningCost
                curCustomers -= 4
            else:
                curProfit += curCustomers * boardingCost - runningCost
                curCustomers = 0
            if curProfit > maxProfit:
                maxProfit = curProfit
                ans = rounds
        while curCustomers > 0:
            rounds += 1
            if curCustomers>=4:
                curProfit += 4 * boardingCost - runningCost
                curCustomers -= 4
            else:
                curProfit += curCustomers * boardingCost - runningCost
                curCustomers = 0
            if curProfit > maxProfit:
                maxProfit = curProfit
                ans = rounds
        return ans

