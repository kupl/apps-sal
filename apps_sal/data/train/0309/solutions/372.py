class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # let dp[i][k] is the length of the arith seq with step size k
        # range is -500, 500
        n = len(A)
        m = 1001
        dp = [[1] * (m + 1) for _ in range(n)]  # can replace it by a dict, will be quicker
        ans = float('-inf')
        for i in range(1, n):
            for k in range(i):
                dp[i][A[i] - A[k] + 500] = max(dp[i][A[i] - A[k] + 500], 1 + dp[k][A[i] - A[k] + 500])  # a_i - a_{i-1} = j
            ans = max(max(dp[i]), ans)
        return ans
