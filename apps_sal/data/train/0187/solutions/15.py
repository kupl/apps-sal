class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans, board, wait = 0, 0, 0
        mc, mv, c = 0, 0, 0
        for cur in customers:
            c += 1  # for counting in which time we are just rotating the wheel
            if cur >= 4 or cur + wait >= 4:
                ans += 4 * boardingCost - runningCost
                wait += cur - 4
            else:
                ans += (cur + wait) * boardingCost - runningCost
                wait = 0

            # for finding the maximum
            if ans > mv:
                mv = ans
                mc = c
        # if still wait is there means we will calculate the ans
        while wait > 0:
            c += 1
            if wait >= 4:
                ans += 4 * boardingCost - runningCost

            else:
                ans += wait * boardingCost - runningCost
            wait -= 4
            # for finding the maximum
            if ans > mv:
                mv = ans
                mc = c
        return mc if mc > 0 else -1
