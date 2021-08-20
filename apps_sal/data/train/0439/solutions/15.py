class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(set(A)) == 1:
            return 1
        dp_less = [0] * len(A)
        dp_more = [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                dp_more[i] = max(2, dp_less[i - 1] + 1)
            elif A[i] < A[i - 1]:
                dp_less[i] = max(2, dp_more[i - 1] + 1)
        return max(max(dp_less), max(dp_more))
