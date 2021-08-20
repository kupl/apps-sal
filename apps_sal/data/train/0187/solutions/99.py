class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        cnt = -1
        wait = 0
        profit = 0
        i = 0
        while wait > 0 or i < len(customers):
            if i < len(customers):
                wait += customers[i]
            if wait >= 4:
                wait -= 4
                profit += 4 * boardingCost
            else:
                profit += wait * boardingCost
                wait = 0
            profit -= runningCost
            i += 1
            if profit > res:
                res = profit
                cnt = i
        return cnt
