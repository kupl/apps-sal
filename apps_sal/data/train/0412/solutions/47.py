
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(h, d, target):
            if not d and not target:
                return 1

            if (d, target) in h:
                return h[(d, target)]
            res = 0
            for i in range(1, f + 1):
                if target - i >= 0 and d > 0:
                    res += helper(h, d - 1, target - i)
            h[(d, target)] = res
            return h[(d, target)]

        h = {}
        return helper(h, d, target) % (10 ** 9 + 7)
