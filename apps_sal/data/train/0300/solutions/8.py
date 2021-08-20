from functools import lru_cache


class Solution:

    @lru_cache(None)
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        if x == target:
            return 0
        if x > target:
            return min(target * 2 - 1, (x - target) * 2)
        (sums, cnt) = (x, 0)
        while sums < target:
            sums *= x
            cnt += 1
        if sums == target:
            return cnt
        (left, right) = (float('inf'), float('inf'))
        if sums - target < target:
            right = self.leastOpsExpressTarget(x, sums - target) + cnt + 1
        left = self.leastOpsExpressTarget(x, target - sums // x) + cnt
        return min(left, right)
