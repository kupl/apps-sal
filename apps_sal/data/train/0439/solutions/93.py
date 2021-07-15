class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        j, ans = 0, 1
        for i, a in enumerate(A[1:], 1):
            if A[i] == A[i - 1]:
                j = i
            elif i == len(A) - 1 or not (A[i - 1] > A[i] < A[i + 1] or A[i - 1] < A[i] > A[i + 1]):
                ans = max(ans, i - j + 1)
                j = i
        return ans
