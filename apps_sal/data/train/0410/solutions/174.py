class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}

        def getPower(x):
            if x in memo:
                return memo[x]
            elif x % 2 == 0:
                memo[x] = 1 + getPower(x / 2)
            else:
                memo[x] = 1 + getPower(3 * x + 1)
            return memo[x]
        return sorted([(getPower(x), x) for x in range(lo, hi + 1)])[k - 1][1]
