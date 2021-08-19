class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        if len(A) == 1:
            return 0
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            this_max = max(A[i] + K, A[-1] - K)
            this_min = min(A[0] + K, A[i + 1] - K)
            res = min(res, this_max - this_min)
        return res
