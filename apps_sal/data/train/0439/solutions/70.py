class Solution:

    def compare(self, m, n):
        if m < n:
            return -1
        elif m > n:
            return 1
        else:
            return 0

    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        ans = 1
        anchor = 0
        for i in range(1, N):
            c = self.compare(A[i - 1], A[i])
            if c == 0:
                anchor = i
            elif i == N - 1 or c * self.compare(A[i], A[i + 1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
