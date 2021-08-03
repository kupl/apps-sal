class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []

        for i, x in enumerate(A):
            Dict = collections.defaultdict(int)
            dp.append(Dict)
            for j in range(i):
                diff = x - A[j]
                dp[i][diff] = dp[j][diff] + 1

        return max(max(y.values()) for y in dp) + 1
