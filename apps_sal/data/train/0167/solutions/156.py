class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[k, n]
            res = float('inf')
            (lo, hi) = (1, n)
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                elif not_broken > broken:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
                elif not_broken == broken:
                    res = min(res, broken + 1)
                    break
            memo[k, n] = res
            return res
        return dp(K, N)
