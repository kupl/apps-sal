class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        turb0 = [1 for i in range(len(A))]
        turb1 = [1 for i in range(len(A))]
        if len(A) <= 1:
            return len(A)
        for i in range(1, len(A)):
            if i % 2 == 0:
                if A[i] > A[i - 1]:
                    turb0[i] = turb0[i - 1] + 1
                elif A[i] < A[i - 1]:
                    turb1[i] = turb1[i - 1] + 1
            elif A[i] > A[i - 1]:
                turb1[i] = turb1[i - 1] + 1
            elif A[i] < A[i - 1]:
                turb0[i] = turb0[i - 1] + 1
        return max(max(turb0), max(turb1))
