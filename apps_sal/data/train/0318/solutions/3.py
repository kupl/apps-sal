from functools import lru_cache


class Solution:

    def maxSizeSlices(self, w: List[int]) -> int:
        n = len(w)
        k = n // 3
        results = [0, 0]
        for offset in range(2):
            cur = [0] * n
            prev = [0] * n
            for i in range(1, k + 1):
                cur[1] = w[offset]
                for j in range(2, n):
                    cur[j] = max(prev[j - 2] + w[j - 1 + offset], cur[j - 1])
                prev = cur
                cur = [0] * n
            results[offset] = prev[-1]
        return max(results)
