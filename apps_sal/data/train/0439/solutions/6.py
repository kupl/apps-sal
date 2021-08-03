class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        asc, desc, res = 1, 1, 1

        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                desc = asc + 1
                asc = 1
            elif A[i] > A[i - 1]:
                asc = desc + 1
                desc = 1
            else:
                asc = 1
                desc = 1

            res = max(max(asc, desc), res)

        return res
