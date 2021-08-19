class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        cache = {}

        def helper(d, target):
            if d == 0 and target == 0:
                return 1
            if d == 0:
                return 0
            if (d, target) in cache:
                return cache[d, target]
            result = 0
            for i in range(max(0, target - f), target):
                result += helper(d - 1, i)
            cache[d, target] = result
            return result
        return helper(d, target) % (10 ** 9 + 7)
