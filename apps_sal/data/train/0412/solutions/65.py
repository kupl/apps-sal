class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def helper(d, target):
            if d == 0 and target == 0:
                return 1
            if d == 0 or target == 0:
                return 0
            if (d, target) in memo:
                return memo[d, target]
            else:
                ans = 0
                for i in range(1, f + 1):
                    ans += helper(d - 1, target - i)
                memo[d, target] = ans % (10 ** 9 + 7)
                return memo[d, target]
        return helper(d, target)
