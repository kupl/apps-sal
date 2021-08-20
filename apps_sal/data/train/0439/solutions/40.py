class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        dp = [0 for _ in range(len(A))]
        dp[0] = 1
        dp[1] = 2 if A[1] != A[0] else 1
        for i in range(2, len(A)):
            if A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]:
                dp[i] = dp[i - 1] + 1
            elif A[i] == A[i - 1]:
                dp[i] = 1
            else:
                dp[i] = 2
        print(dp)
        return max(dp)

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        curr_max = global_max = 1
        for i in range(1, len(A)):
            if i >= 2 and A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]:
                curr_max += 1
            elif i >= 1 and A[i - 1] != A[i]:
                curr_max = 2
            else:
                curr_max = 1
            global_max = max(global_max, curr_max)
        return global_max
