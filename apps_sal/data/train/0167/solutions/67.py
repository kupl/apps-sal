class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(K, N):
            if (K, N) in memo:
                return memo[(K, N)]

            if K == 1:
                return N
            if N == 0:
                return 0

            res = sys.maxsize

            # for i in range(1, N + 1):
            #     res = min(res, max(dp(K - 1, i - 1), dp(K, N - i)) + 1)
            lo, hi = 1, N
            while lo <= hi:
                mid = int(lo + (hi - lo) / 2)
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)

                if broken < not_broken:
                    lo = mid + 1
                    res = min(not_broken + 1, res)
                else:
                    hi = mid - 1
                    res = min(broken + 1, res)

            memo[(K, N)] = res

            return res

        return dp(K, N)
