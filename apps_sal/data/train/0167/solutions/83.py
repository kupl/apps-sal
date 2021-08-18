class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        def dfs(k, n, memo):

            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]

            res = float('inf')

            lo, hi = 1, n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dfs(k - 1, mid - 1, memo)
                no_broken = dfs(k, n - mid, memo)
                if broken > no_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, no_broken + 1)
            memo[(k, n)] = res
            return res
        return dfs(K, N, {})
