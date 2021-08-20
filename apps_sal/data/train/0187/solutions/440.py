class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (self.wait, self.count, self.ans, self.total, self.max_profit) = (0, 0, 0, 0, 0)

        def helper(num):
            temp = self.wait + num
            if temp >= 4:
                board = 4
                temp -= 4
            else:
                board = temp
                temp = 0
            self.wait = temp
            self.count += 1
            self.total += board * boardingCost - runningCost
            if self.total > self.max_profit:
                self.max_profit = self.total
                self.ans = self.count
        for num in customers:
            helper(num)
        while self.wait > 0:
            helper(0)
        return self.ans if self.ans != 0 else -1
