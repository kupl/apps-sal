class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        i = 0
        k = 1
        count = 0
        N = len(A)
        ans = 0
        anchor = 0
        max1 = 0
        while i <= k and k < len(A):
            if A[k - 1] > A[k] and k % 2 == 0:
                count += 1
                k += 1
            elif A[k - 1] < A[k] and k % 2 != 0:
                count += 1
                k += 1
            else:
                i = k
                k = i + 1
                max1 = max(max1, count)
                count = 0
        max1 = max(max1, count) + 1
        i = 0
        k = 1
        max2 = 0
        count = 0
        while i <= k and k < len(A):
            if A[k - 1] > A[k] and k % 2 != 0:
                count += 1
                k += 1
            elif A[k - 1] < A[k] and k % 2 == 0:
                count += 1
                k += 1
            else:
                i += 1
                k = i + 1
                max2 = max(max2, count)
                count = 0
        max2 = max(max2, count) + 1
        return max(max1, max2)
