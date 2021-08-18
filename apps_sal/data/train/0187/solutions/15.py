class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans, board, wait = 0, 0, 0
        mc, mv, c = 0, 0, 0
        for cur in customers:
            c += 1
            if cur >= 4 or cur + wait >= 4:
                ans += 4 * boardingCost - runningCost
                wait += cur - 4
            else:
                ans += (cur + wait) * boardingCost - runningCost
                wait = 0

            if ans > mv:
                mv = ans
                mc = c
        while wait > 0:
            c += 1
            if wait >= 4:
                ans += 4 * boardingCost - runningCost

            else:
                ans += wait * boardingCost - runningCost
            wait -= 4
            if ans > mv:
                mv = ans
                mc = c
        return mc if mc > 0 else -1
