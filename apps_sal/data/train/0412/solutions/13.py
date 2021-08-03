class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def helper(rolls_left, t):
            if not t and not rolls_left:
                return 1
            if not rolls_left or not t:
                return 0
            ret = 0
            for v in range(1, min(f + 1, t + 1)):
                if (rolls_left - 1, t - v) not in memo:
                    memo[(rolls_left - 1, t - v)] = helper(rolls_left - 1, t - v)
                ret += memo[(rolls_left - 1, t - v)]
            return ret
        return helper(d, target) % (10**9 + 7)
