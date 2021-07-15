class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for _ in range(n)]
        ans = 2
        for i in range(1, n):
            for j in range(i):
                key_i = (A[i], A[i] - A[j])
                key_j = (A[j], A[i] - A[j])
                if key_i not in dp[i]:
                    dp[i][key_i] = 2
                if key_j in dp[j]:
                    dp[i][key_i] = max(dp[i][key_i], dp[j][key_j] + 1)
                ans = max(dp[i][key_i], ans)
        return ans
