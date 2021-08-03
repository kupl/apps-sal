class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total, board = 0, 0
        ans = 1
        res = 1
        m = -1

        def cal():
            nonlocal total, ans, res, m, board
            t = 4 if total >= 4 else total
            total -= t
            board += t
            cost = board * boardingCost - ans * runningCost
            if cost > m:
                m = cost
                res = ans
            ans += 1

        for c in customers:
            total += c
            cal()

        while total > 0:
            cal()
        return res if m >= 0 else -1
