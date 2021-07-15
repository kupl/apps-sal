class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        minLeft, maxRight = [A[0]] * n, [A[-1]] * n
        for i in range(1, n):
            minLeft[i] = min(minLeft[i - 1], A[i])
            maxRight[n - i - 1] = max(maxRight[n - i], A[n - i - 1])
        i = j = n - 1
        res = 0
        while i >= 0 and j >= 0:
            if minLeft[i] <= maxRight[j]:
                res = max(res, j - i)
                i -= 1
            else:
                j -= 1
        return res
