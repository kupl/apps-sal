class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        store = {}

        def helper(d, f, target):
            if d == 0 or f == 0 or target <= 0:
                return 0
            if d == 1 and target > f:
                return 0
            if d == 1 and target <= f:
                return 1

            if (d, f, target) in store:
                return store[(d, f, target)]

            n = 0
            for i in range(1, f + 1):
                n += helper(d - 1, f, target - i)

            store[(d, f, target)] = n
            return n

        return (helper(d, f, target)) % (10**9 + 7)
