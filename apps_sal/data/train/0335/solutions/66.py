class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {}
        dp[0] = 0

        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s + i] = max(dp[s] + i, cur[s + i])
                cur[s] = max(dp[s], cur[s])
                cur[s - i] = max(dp[s], cur[s - i])
            dp = cur
        return dp[0]


#         total = sum(rods)
#         n = len(rods)
#         m = total // 2
#         dp = [0] * (m + 1)
#         for i in range(n):
#             for j in range(m, rods[i] - 1, -1):
#                 dp[j] = max(dp[j], dp[j - rods[i]] + rods[i])
#         print(dp)
