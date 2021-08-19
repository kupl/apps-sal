class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(k, n):
            if n == 0:
                return 0
            if k == 1:
                return n
            if (k, n) in memo:
                return memo[k, n]
            res = float('inf')
            lo = 1
            hi = n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[k, n] = res
            return res
        return dp(K, N)
