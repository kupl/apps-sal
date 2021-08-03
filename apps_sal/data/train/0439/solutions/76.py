class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        result = 1
        left = 0

        def cmp(a, b):
            return (a > b) - (a < b)
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                left = i
            elif i == len(A) - 1 or cmp(A[i], A[i - 1]) * cmp(A[i + 1], A[i]) != -1:
                result = max(result, i + 1 - left)
                left = i
        return result
