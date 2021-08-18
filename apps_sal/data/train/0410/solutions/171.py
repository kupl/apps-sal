class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        memo = {}

        def help(x):
            if x in memo:
                return memo[x]

            if x == 1:
                return 0

            if x % 2 == 0:
                memo[x] = 1 + help(x // 2)
            else:
                memo[x] = 1 + help(x * 3 + 1)

            return memo[x]

        return sorted(list(range(lo, hi + 1)), key=lambda x: [help(x), x])[k - 1]
