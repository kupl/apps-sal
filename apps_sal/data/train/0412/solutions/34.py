class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        D = {}

        def func(d, f, target):
            res = 0
            if d == 0 and target == 0:
                return 1
            if d == 0 and target != 0:
                return 0
            if target < 0:
                return 0

            for i in range(1, f + 1):
                if (d - 1, target - i) not in D:
                    D[d - 1, target - i] = func(d - 1, f, target - i)
                res += D[d - 1, target - i]
                res = res % (10**9 + 7)
            return res

        return func(d, f, target)
