class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        cumsum = [A[0]]
        for i in range(1, len(A)):
            cumsum.append(cumsum[-1] + A[i])
        cumsum.append(0)

        @lru_cache(None)
        def rec(i, K):
            if K == 1:
                return (cumsum[len(A) - 1] - cumsum[i - 1]) / (len(A) - i)
            return max(((cumsum[j] - cumsum[i - 1]) / (j - i + 1) + rec(j + 1, K - 1) for j in range(i, len(A) - K + 1)))
        return rec(0, K)
