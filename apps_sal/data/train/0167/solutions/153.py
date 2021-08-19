import sys


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        val = Solution.dp(K, N)
        return val
    __memo = dict()

    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0
        if (K, N) in Solution.__memo:
            return Solution.__memo[(K, N)]
        res = sys.maxsize
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = Solution.dp(K - 1, mid - 1)  # 碎
            not_broken = Solution.dp(K, N - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        Solution.__memo[(K, N)] = res
        return res
