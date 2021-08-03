class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        A.sort()
        x = A[0]
        y = A[-1]
        res = y - x
        for i in range(len(A)):
            A[i] += 2 * K
            x = min(A[0], A[(i + 1) % len(A)])
            y = max(A[i], y)
            res = min(res, y - x)
        return res
