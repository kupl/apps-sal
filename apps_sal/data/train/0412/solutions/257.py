class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def rec_find_target_sum(d, f, target):
            if (d, f, target) in memo:
                return memo[d, f, target]
            if d == 0 or d * f < target or target <= 0:
                return 0
            if d == 1:
                return 1
            possibs = 0
            for face in range(f):
                possibs += rec_find_target_sum(d - 1, f, target - face - 1)
            memo[d, f, target] = possibs
            return possibs
        memo = {}
        return rec_find_target_sum(d, f, target) % (10 ** 9 + 7)
