class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def power(n):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]
            if n % 2 == 0:
                res = 1 + power(n / 2)
            else:
                res = 1 + power(3 * n + 1)
            memo[n] = res
            return res
        s = sorted(range(lo, hi + 1), key=power)
        return s[k - 1]
