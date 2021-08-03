class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        dp = [0] * len(customers)
        num_shift = 0
        num_wait = 0
        profit = 0
        total_board = 0

        for i in range(len(customers)):
            arr = customers[i]
            if num_wait + arr <= 4:
                num_wait = 0
                total_board += arr
            else:
                num_wait = num_wait + arr - 4
                total_board += 4
            num_shift += 1
            dp[i] = total_board * boardingCost - num_shift * runningCost

        while num_wait > 0:
            total_board += min(num_wait, 4)
            num_wait -= min(num_wait, 4)
            num_shift += 1
            dp.append(total_board * boardingCost - num_shift * runningCost)

        if max(dp) > 0:
            return dp.index(max(dp)) + 1
        else:
            return -1
