class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        dp = [0] * max(len(customers) + 1, sum(customers) // 4 + 2)
        total = 0
        for i in range(1, len(dp)):
            if i < len(customers) + 1:
                total += customers[i - 1]
            if total > 0 and total < 4:
                dp[i] = total * boardingCost - runningCost + dp[i - 1]
            elif total > 0 and total >= 4:
                dp[i] = 4 * boardingCost - runningCost + dp[i - 1]
                total -= 4
        (amount, cycle) = max([(money, index) for (index, money) in enumerate(dp)], key=lambda x: (x[0], -x[1]))
        return cycle if amount > 0 else -1
