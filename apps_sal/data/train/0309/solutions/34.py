class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        for i in range(len(A)):
            nd = collections.defaultdict(int)
            dp.append(nd)
            for j in range(i):
                curr_diff = A[i] - A[j]
                dp[i][curr_diff] = dp[j][curr_diff] + 1
        maxVal = -99999
        for dt in dp:
            maxVal = max(maxVal, max(dt.values()) + 1)
        return maxVal
