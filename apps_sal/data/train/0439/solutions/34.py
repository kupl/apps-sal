class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = 1
        pre = 0
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                pre = i + 1
            elif i == len(A) - 2 or self.cmp(A[i], A[i + 1]) * self.cmp(A[i + 1], A[i + 2]) != -1:
                res = max(res, i + 2 - pre)
                pre = i + 1
        return res

    def cmp(self, a, b):
        return (a > b) - (a < b)
