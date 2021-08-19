class Solution:

    def cmp(self, a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    def maxTurbulenceSize(self, A: List[int]) -> int:
        ans = 1
        index = 0
        for i in range(1, len(A)):
            k = self.cmp(A[i - 1], A[i])
            if k == 0:
                index = i
            elif i == len(A) - 1 or k * self.cmp(A[i], A[i + 1]) != -1:
                ans = max(ans, i - index + 1)
                index = i
        return ans
