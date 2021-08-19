class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        # https://leetcode.com/problems/shortest-common-supersequence/discuss/639784/Python-DP-with-detailed-explanation
        # https://leetcode.com/problems/shortest-common-supersequence/discuss/674175/Python-Very-simple-solution-with-DP-Table-Memory-95

        m, n = len(str1) + 1, len(str2) + 1
        dp = [''] * n
        for c in range(n):
            dp[c] = str2[:c]
        for r in range(1, m):
            pre = dp[:]  # use pre to store last row's information
            dp[0] += str1[r - 1]
            for c in range(1, n):
                if str1[r - 1] == str2[c - 1]:
                    dp[c] = pre[c - 1] + str1[r - 1]
                else:
                    if len(pre[c]) < len(dp[c - 1]):
                        dp[c] = pre[c] + str1[r - 1]
                    else:
                        dp[c] = dp[c - 1] + str2[c - 1]
        return dp[-1]
