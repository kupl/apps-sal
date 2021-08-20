class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        profit = 0
        ans = -1
        count = 0
        for i in customers:
            count += 1
            q += i
            board = min(q, 4)
            q -= board
            temp = profit + board * boardingCost - runningCost
            if temp > profit:
                profit = temp
                ans = count
        times = q // 4
        left = q % 4
        temp = profit + times * (4 * boardingCost - runningCost)
        if temp > profit:
            profit = temp
            count += times
            ans = count
        temp = profit + left * boardingCost - runningCost
        if temp > profit:
            profit = temp
            count += 1
            ans = count
        return ans
