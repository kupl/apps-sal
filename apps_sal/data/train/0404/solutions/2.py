from functools import lru_cache
from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        n = len(A)
        p = [0] + list(accumulate(A))

        @lru_cache(None)
        def dp(l, k):
            if k > l:
                return 0
            if k == 1:
                return p[l] / l
            return max(dp(i, k - 1) + (p[l] - p[i]) / (l - i) for i in range(k - 1, l))
        return dp(n, K)
