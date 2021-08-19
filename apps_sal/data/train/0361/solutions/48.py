class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(n, m):
            """
            Returns the min num of square blocks for nxm rectangle
            """
            (p, q) = (min(n, m), max(n, m))
            if p == 0:
                return 0
            if p == 1:
                return q
            if q % p == 0:
                return q // p
            minunits = p * q
            for r in range(1, p):
                minunits = min(minunits, 1 + dp(p - r, r) + dp(p, q - r))
                minunits = min(minunits, 1 + dp(q - r, r) + dp(q, p - r))
            for cl in range(1, n):
                for cr in range(1, n - cl):
                    for rl in range(1, m):
                        for rr in range(1, m - rl):
                            minunits = min(minunits, dp(rl, n - cr) + dp(m - rl, cl) + dp(n - cl, rr) + dp(m - rr, cr) + dp(n - cl - cr, m - rl - rr))
            return minunits
        return dp(n, m)
