class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        # Top down: Time O(KN log(N)) Space O(KN)
        import functools
        @functools.lru_cache(None)
        def dp(k, m):
            if k == 1: return m
            if m == 1: return 1
            return dp(k-1, m-1) + dp(k, m-1) + 1
        l, r = 1, N
        while l < r:
            mid = (l+r) // 2
            if dp(K, mid) >= N:
                r = mid
            else:
                l = mid + 1
        return l
        '''
        # Bottom up: Time O(Klog(N)) Space O(K)
        dp, ndp = {}, {}
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                if m == 1:
                    ndp[k] = 1
                elif k == 1:
                    ndp[k] = m
                else:
                    ndp[k] = dp[k - 1] + dp[k] + 1
                if ndp[k] >= N:
                    return m
            dp, ndp = ndp, {}
