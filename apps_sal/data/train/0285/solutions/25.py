class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        minV, maxV = A[0], A[-1]
        res = maxV - minV
        for i in range(len(A) - 1):
            A[i] += 2 * K
            maxV = max(maxV, A[i])
            minV = min(A[0], A[i + 1])
            res = min(res, maxV - minV)
        return res
