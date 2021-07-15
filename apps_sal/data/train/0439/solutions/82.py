class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = curr = 0
        for i in range(len(A)):
            if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
                curr += 1
            elif i >= 1 and A[i-1] != A[i]:
                curr = 2
            else:
                curr = 1
            res = max(res, curr)
        return res
