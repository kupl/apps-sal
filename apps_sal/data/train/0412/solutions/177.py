class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def auxNumRolls(d, f, target, memoization):
            if target < d or target > d * f:
                return 0
            if d == 1:
                return 1
            ans = 0
            for i in range(1, f + 1):
                if (d - 1, target - i) not in memoization:
                    memoization[d - 1, target - i] = auxNumRolls(d - 1, f, target - i, memoization)
                ans += memoization[d - 1, target - i]
            return ans
        return auxNumRolls(d, f, target, {}) % (10 ** 9 + 7)
