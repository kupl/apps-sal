class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def maxAverage(j, k):
            if j == k:
                return sum(A[:j])
            if k == 1:
                return sum(A[:j]) / j
            ans = 0
            for i in range(j - 1, max(-1, k - 2), -1):
                ans = max(ans, (sum(A[i:j])) / (j - i) + maxAverage(i, k - 1))
            return ans
        return maxAverage(len(A), K)
