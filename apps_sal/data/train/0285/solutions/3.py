class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        diff = A[-1] - A[0]
        for i in range(len(A) - 1):
            lower = min(A[0] + 2 * K, A[i + 1])
            upper = max(A[-1], A[i] + 2 * K)
            diff = min(diff, abs(upper - lower))
        return diff
