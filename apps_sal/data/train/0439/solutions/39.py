class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        n = len(A)
        dp = [1] * len(A)
        prev_sign = ''

        for i in range(1, n):
            curr_sign = '<' if A[i] < A[i - 1] else '>'
            curr_sign = '=' if A[i] == A[i - 1] else curr_sign
            if curr_sign == '=':
                prev_sign = ''
                continue
            if prev_sign != curr_sign:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] += 1
            prev_sign = curr_sign

        return max(dp)
