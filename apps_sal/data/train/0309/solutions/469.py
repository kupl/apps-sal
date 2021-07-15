class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A: return 0
        dp = [{} for _ in range(len(A))]
        res = 0
        for j in range(1, len(A)):
            for i in range(j):
                if A[j]-A[i] in dp[i]:
                    dp[j][A[j]-A[i]] = dp[i][A[j]-A[i]]+1
                else:
                    dp[j][A[j]-A[i]] = 1
                res = max(dp[j][A[j]-A[i]], res)
        return res+1

