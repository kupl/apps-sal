class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for s1_index in range(len(s1)):
            for s2_index in range(len(s2)):
                if s1[s1_index] != s2[s2_index]:
                    dp[s1_index + 1][s2_index + 1] = max(dp[s1_index][s2_index + 1],
                                                         dp[s1_index + 1][s2_index],
                                                         dp[s1_index][s2_index])
                else:
                    dp[s1_index + 1][s2_index + 1] = max(dp[s1_index][s2_index + 1],
                                                         dp[s1_index + 1][s2_index],
                                                         dp[s1_index][s2_index] + 1)
        return dp[-1][-1]
