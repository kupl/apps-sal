from collections import defaultdict
MOD = (10 ** 9) + 7


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        if target > f * d:
            return 0
        if target == f * d:
            return 1

        def F(j, memo, left):
            if (j, left) in memo.keys():
                return memo[(j, left)]

            if left < 0:
                return 0

            if j == d - 1:
                memo[(j, left)] = int(left <= f and left >= 1)
                return memo[(j, left)]

            ans = 0
            for i in range(1, f + 1):
                ans += F(j + 1, memo, left - i)

            memo[(j, left)] = ans
            return memo[(j, left)]

        F(0, memo, target)

        return memo[(0, target)] % MOD
