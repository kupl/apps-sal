class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[-1], A[i] + 2 * K)
            small = min(A[0] + 2 * K, A[i + 1])
            res = min(res, big - small)
        return res
