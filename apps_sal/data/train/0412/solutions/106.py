class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def rec(d, target):
            if d == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if target <= 0:
                return 0
            if (d, target) in memo:
                return memo[d, target]
            count = 0
            for i in range(1, f + 1):
                count += rec(d - 1, target - i)
            memo[d, target] = count
            return count
        return rec(d, target) % (10 ** 9 + 7)
