class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        if A[-1] - A[0] <= K:
            return A[-1] - A[0]
        else:
            res = A[-1] - A[0]
            for i in range(len(A) - 1):
                res = min(res, max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K))
            return res
