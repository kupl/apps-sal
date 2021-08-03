class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(K, N):
            if N == 0:
                return 0
            if K == 1:
                return N

            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')

            # for i in range(1, N+1):
            #     res = min(res, max(dp(K-1, i-1),  dp(K, N-i))+1)

            lo, hi = 1, N

            while(lo <= hi):
                mid = lo + (hi - lo) // 2
                broken = dp(K - 1, mid - 1)
                unbroken = dp(K, N - mid)
                if broken > unbroken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, unbroken + 1)

            memo[(K, N)] = res
            return res
        return dp(K, N)
