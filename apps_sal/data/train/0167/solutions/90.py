class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            l, h = 1, N
            while l <= h:
                mid = (l + h) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    h = mid - 1
                    res = min(res, 1 + broken)
                else:
                    l = mid + 1
                    res = min(res, 1 + not_broken)
            memo[(K, N)] = res
            return res
        return dp(K, N)
