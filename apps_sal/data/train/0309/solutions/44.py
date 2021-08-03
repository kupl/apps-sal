class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        max_l = 2
        dp = [{0: 1}]
        for i in range(1, len(A)):
            dp.append({})
            for j in range(0, i):
                idx = A[i] - A[j]
                if idx in dp[j]:
                    dp[i][idx] = dp[j][idx] + 1
                    max_l = max(max_l, dp[i][idx])
                else:
                    dp[i][idx] = 2
        return max_l
