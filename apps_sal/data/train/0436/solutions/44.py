class Solution:

    def minDays(self, n: int) -> int:
        m = collections.defaultdict(int)
        m[0] = 0
        m[1] = 1

        def helper(n):
            if n in m:
                return m[n]
            res = float('inf')
            if n % 3 == 0:
                res = min(res, 1 + helper(n // 3))
            if n % 2 == 0:
                res = min(res, 1 + helper(n // 2))
            if n % 3 == 1:
                res = min(res, 1 + helper(n - 1))
            if n % 3 == 2:
                res = min(res, 2 + helper(n - 2))
            if n % 2 != 0:
                res = min(res, 1 + helper(n - 1))
            m[n] = res
            return res
        return helper(n)
