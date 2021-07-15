class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        dp = []
        max_length = 0
        for i in range(len(A)):
            nd = defaultdict(int)
            nd[0] = 1
            dp.append(nd)
            for j in range(i):
                diff = A[i]-A[j]
                dp[i][diff] = max(dp[j][diff],1)+1
                if dp[i][diff] > max_length:
                    max_length = dp[i][diff]
        return max_length
