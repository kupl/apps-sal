class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in A]
        max_l = 1
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                if dp[i][diff] > max_l:
                    max_l = dp[i][diff]
        return max_l
