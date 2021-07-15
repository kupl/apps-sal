class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        for i in range(len(A)):
            dp.append(collections.defaultdict(lambda: 1))
            for j in range(i):
                # calculate the differences
                diff = A[i] - A[j]
                # check the existing sequence length
                dp[i][diff] = max(dp[i][diff], dp[j][diff]+1)
        return max([max(d.values()) for d in dp])

