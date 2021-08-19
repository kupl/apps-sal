class Solution:

    def smallestRangeII(self, A: List[int], k: int) -> int:
        A.sort()
        n = len(A)
        res = A[n - 1] - A[0]
        for i in range(n - 1):
            mn = min(A[i + 1] - k, A[0] + k)
            mx = max(A[i] + k, A[n - 1] - k)
            res = min(res, mx - mn)
        return res
