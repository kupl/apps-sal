class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        ans = 0
        cur = 0
        for i in range(len(A)):
            if i >= 2 and (A[i] > A[i - 1] < A[i - 2] or A[i] < A[i - 1] > A[i - 2]):
                cur += 1
            elif i >= 1 and A[i] != A[i - 1]:
                cur = 2
            else:
                cur = 1
            ans = max(ans, cur)
        return ans
