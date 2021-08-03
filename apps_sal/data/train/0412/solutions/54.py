class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def helper(d, target):
            if d == 0 and target == 0:
                return 1
            if d == 0:
                return 0
            if (target, d) in memo:
                return memo[(target, d)]
            num_ways = 0
            for i in range(1, f + 1):
                if target - i >= 0:
                    num_ways += helper(d - 1, target - i)
            memo[(target, d)] = num_ways
            return num_ways

        return helper(d, target) % (10**9 + 7)
