class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ans = 1
        for x in range(len(A)):
            for y in range(x + 1, len(A)):
                dp[y, A[y] - A[x]] = dp.get((x, A[y] - A[x]), 1) + 1
                ans = max(dp[y, A[y] - A[x]], ans)
        return ans
