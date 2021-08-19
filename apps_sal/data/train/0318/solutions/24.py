from functools import lru_cache


class Solution:

    def maxSizeSlices(self, w: List[int]) -> int:
        n = len(w)
        k = n // 3
        dp1 = [[0] * n for _ in range(k + 1)]
        results = [0, 0]
        for offset in range(2):
            for i in range(1, k + 1):
                dp1[i][1] = w[offset]
                for j in range(2, n):
                    dp1[i][j] = max(dp1[i - 1][j - 2] + w[j - 1 + offset], dp1[i][j - 1])
            results[offset] = dp1[-1][-1]
        return max(results)
