from functools import lru_cache
import itertools


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # Time  complexity: O(N^3 / K)
        # Space complexity: O(KN^2)
        n = len(stones)
        if (n - 1) % (K - 1):
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K:
                return 0

            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))

            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]

            return res

        return dp(0, n - 1)
