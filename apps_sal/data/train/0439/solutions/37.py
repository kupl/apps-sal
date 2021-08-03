class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0
        dp_GT = [1] * len(A)
        dp_LT = [1] * len(A)
        for n in range(1, len(A)):
            if A[n] > A[n - 1]:
                dp_GT[n] = dp_LT[n - 1] + 1
                dp_LT[n] = 1
            elif A[n] < A[n - 1]:
                dp_LT[n] = dp_GT[n - 1] + 1
                dp_GT[n] = 1
            else:
                dp_LT[n] = 1
                dp_GT[n] = 1
#        print(\"dp_GT \",dp_GT)
 #       print(\"dp_LT \",dp_LT)
        return max(max(dp_GT), max(dp_LT))
