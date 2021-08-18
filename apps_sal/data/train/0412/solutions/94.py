from collections import defaultdict


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = defaultdict(int)

        def helper(d, target):
            if d == 0:
                return 1 if target == 0 else 0
            if (d, target) in memo:
                return memo[(d, target)]

            for c in range(1, f + 1):
                memo[(d, target)] += helper(d - 1, target - c)
            return memo[(d, target)]
        return helper(d, target) % (10**9 + 7)
