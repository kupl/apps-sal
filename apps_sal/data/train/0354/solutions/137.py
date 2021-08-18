class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        d = {}

        def dp(n, v, k):

            if n == 1:
                return 1
            if (n, v, k) not in d:
                if k == 1:
                    d[(n, v, k)] = 0
                    for i, lim in enumerate(rollMax):
                        if i != v:
                            d[(n, v, k)] += dp(n - 1, i, lim)
                elif k == 2:
                    d[(n, v, k)] = dp(n, v, 1) + dp(n - 1, v, k - 1)
                else:
                    d[(n, v, k)] = dp(n, v, k - 1) + dp(n - 1, v, k - 1) - dp(n - 1, v, k - 2)
            return d[(n, v, k)]

        def get_exact(n, v, k):
            if k == 1:
                return dp(n, v, k)
            return dp(n, v, k) - dp(n, v, k - 1)

        res = 0
        for i, lim in enumerate(rollMax):
            for j in range(1, lim + 1):
                res += get_exact(n, i, j)

        return res % (10**9 + 7)
