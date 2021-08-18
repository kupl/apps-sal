class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        n = len(customers)
        board = 0
        wait = 0
        ans = -1
        max_profit = 0
        while wait > 0 or i < n:
            if i < n:
                wait += customers[i]
            board += min(4, wait)
            wait = max(0, wait - 4)

            tmp_profit = board * boardingCost - (i + 1) * runningCost
            if tmp_profit > max_profit:
                max_profit = tmp_profit
                ans = i + 1

            i += 1

        return ans
