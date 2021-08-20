class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = []
        maxv = 0
        for i in range(n):
            cur = A[i]
            dp.append({})
            for j in range(i):
                pre = A[j]
                dif = cur - pre
                if dif not in dp[i]:
                    dp[i][dif] = 0
                if dif in dp[j]:
                    dp[i][dif] = dp[j][dif] + 1
                else:
                    dp[i][dif] = 1
                maxv = max(maxv, dp[i][dif])
        return maxv + 1
