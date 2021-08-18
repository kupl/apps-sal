class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        runstart = 0
        maxrun = 1

        prevsign = -2

        for i in range(1, len(A)):

            if A[i] > A[i - 1]:
                sign = 1
            elif A[i] < A[i - 1]:
                sign = -1
            else:
                sign = 0

            if sign != prevsign and sign != 0:
                maxrun = max(maxrun, i - runstart + 1)
            elif sign != 0:
                runstart = i - 1
            else:
                runstart = i

            prevsign = sign

        return maxrun
