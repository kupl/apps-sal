class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        n = len(A)
        if n == 1:
            return 1

        up, down = 1, 1
        ans = 1

        for i in range(1, n):
            if A[i] > A[i - 1]:
                up = down + 1
                down = 1
            elif A[i] < A[i - 1]:
                down = up + 1
                up = 1
            else:
                up, down = 1, 1
            ans = max(ans, down, up)

        return ans
