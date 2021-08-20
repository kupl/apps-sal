class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        cache = {}

        def helper(d, target):
            if target == 0 and d == 0:
                return 1
            if d == 0:
                return 0
            if (d, target) in cache:
                return cache[d, target]
            ways = 0
            for i in range(1, f + 1):
                if target - i >= 0:
                    ways = (ways + helper(d - 1, target - i)) % 1000000007
            cache[d, target] = ways
            return cache[d, target]
        return helper(d, target)
