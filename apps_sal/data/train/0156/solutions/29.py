class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if not str1:
            return str2
        if not str2:
            return str1
        l1, l2 = len(str1), len(str2)
        # Step 1. find a longest common subsequence.
        dp = [''] * (l1 + 1)
        for j in range(l2):
            new_dp = dp[:]
            for i in range(l1):
                if str1[i] == str2[j]:
                    new_dp[i + 1] = dp[i] + str1[i]
                elif len(dp[i + 1]) < len(new_dp[i]):
                    new_dp[i + 1] = new_dp[i]
            dp = new_dp
        # Step 2. make a supersequences from the longest common subsequence.
        ans, i, j = '', 0, 0
        for c in dp[-1]:
            while str1[i] != c:
                ans += str1[i]
                i += 1
            while str2[j] != c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        return ans + str1[i:] + str2[j:]
