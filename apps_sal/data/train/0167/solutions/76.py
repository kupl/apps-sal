class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]

            res = sys.maxsize
            lo, hi = 1, n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(k - 1, mid - 1)
                safe = dp(k, n - mid)
                if broken > safe:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, safe + 1)

            memo[(k, n)] = res
            return res

        memo = {}
        return dp(K, N)
