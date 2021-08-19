class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        A.sort()
        i = 0
        j = len(A) - 1
        min_diff = A[-1] - A[0]
        bottom = A[0]
        peak = A[-1]
        for idx in range(len(A) - 1):
            (current, _next) = (A[idx], A[idx + 1])
            bottom = min(A[0] + K, _next - K)
            peak = max(A[-1] - K, current + K)
            min_diff = min(min_diff, peak - bottom)
        return min_diff
