class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dp = [{} for i in range(len(A))]
        for i in range(len(A)):
            dp[i] = {0: 1}
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

        ans = 0
        for dic in dp:
            if dic:
                ans = max(ans, max(dic.values()))

        return ans
