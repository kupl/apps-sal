class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        @lru_cache(None)
        def calc(goal):
            if x == goal:
                return 0
            if x > goal:
                return min(goal * 2 - 1, (x - goal) * 2)
            sums = x
            times = 0
            while sums < goal:
                times += 1
                sums *= x
            if sums == goal:
                return times
            if sums - goal < goal:
                return min(calc(sums - goal) + times + 1, calc(goal - sums // x) + times)
            return calc(goal - sums // x) + times
        return calc(target)
