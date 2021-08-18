class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        for diff in range(-500, 501):
            dp = defaultdict(int)
            for e in A:
                dp[e] = dp[e - diff] + 1
                ans = max(ans, dp[e])

        return ans
