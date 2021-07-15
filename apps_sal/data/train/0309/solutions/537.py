class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(A))]
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                dp[i][A[i]-A[j]] = max(dp[i][A[i]-A[j]], dp[j].get(A[i]-A[j], 1)+1)
                res = max(res, dp[i][A[i]-A[j]])
        return res
