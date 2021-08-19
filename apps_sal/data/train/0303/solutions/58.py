class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        @lru_cache(None)
        def checkSum(i, j, k):
            if j - i <= k:
                return max(A[i:j]) * (j - i)
            else:
                best = 0
                for nk in range(1, K + 1):
                    best = max(best, checkSum(i, i + nk, K) + checkSum(i + nk, j, K))
            return best
        return checkSum(0, len(A), K)
