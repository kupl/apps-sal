from functools import lru_cache


class Solution:
    def maxSizeSlices(self, w: List[int]) -> int:
        n = len(w)
        k = n // 3
        dp1 = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            dp1[i][1] = w[0]
            for j in range(2, n):
                dp1[i][j] = max(dp1[i - 1][j - 2] + w[j - 1], dp1[i][j - 1])

        r1 = dp1[-1][-1]

        for i in range(1, k + 1):
            dp1[i][1] = w[1]
            for j in range(2, n):
                dp1[i][j] = max(dp1[i - 1][j - 2] + w[j], dp1[i][j - 1])

        return max(dp1[-1][-1], r1)
