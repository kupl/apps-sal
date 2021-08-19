class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        turb0 = 1
        turb1 = 1
        if len(A) <= 1:
            return len(A)  # covers really small cases
        max_val = 1
        for i in range(1, len(A)):
            print((turb0, turb1, i))
            if i % 2 == 0:
                if A[i] > A[i - 1]:
                    turb0 += 1
                    turb1 = 1
                elif A[i] < A[i - 1]:
                    turb1 += 1
                    turb0 = 1
                else:
                    turb0 = 1
                    turb1 = 1
            else:
                if A[i] > A[i - 1]:
                    turb1 += 1
                    turb0 = 1
                elif A[i] < A[i - 1]:
                    turb0 += 1
                    turb1 = 1
                else:
                    turb0 = 1
                    turb1 = 1
            max_val = max(turb0, turb1, max_val)
        return max_val
