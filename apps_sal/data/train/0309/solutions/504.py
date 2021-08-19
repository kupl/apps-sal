from collections import defaultdict


class Solution:

    def find(self, A):
        dp = []
        ans = 1
        for _ in A:
            dp.append({})
        for (i, ai) in enumerate(A):
            for j in range(i):
                aj = A[j]
                d = ai - aj
                if d < 0:
                    continue
                if d not in dp[i]:
                    dp[i][d] = 1
                if d not in dp[j]:
                    dp[j][d] = 1
                temp = max(dp[i][d], dp[j][d] + 1)
                dp[i][d] = temp
                ans = max(ans, temp)
        return ans

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = self.find(A)
        ans = max(ans, self.find(A[::-1]))
        return ans
