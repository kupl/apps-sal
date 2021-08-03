class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp, ans = [], 2
        for i in range(len(A)):
            dp.append({})
            for j in range(i - 1, -1, -1):
                dif = A[i] - A[j]
                if dif not in dp[i]:
                    dp[i][dif] = 2
                if dif in dp[j]:
                    dp[i][dif] = max(dp[j][dif] + 1, dp[i][dif])
                ans = max(ans, dp[i][dif])
        return ans
