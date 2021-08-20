class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def helper(i, j):
            if i < 0 or j < 0:
                return ''
            if str1[i] == str2[j]:
                return helper(i - 1, j - 1) + str1[i]
            return max(helper(i - 1, j), helper(i, j - 1), key=len)
        subseq = helper(len(str1) - 1, len(str2) - 1)
        (ans, i, j) = ('', 0, 0)
        for c in subseq:
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

    def shortestCommonSupersequence_dp(self, str1: str, str2: str) -> str:
        if not str1:
            return str2
        if not str2:
            return str1
        (l1, l2) = (len(str1), len(str2))
        dp = [''] * (l1 + 1)
        for j in range(l2):
            new_dp = dp[:]
            for i in range(l1):
                if str1[i] == str2[j]:
                    new_dp[i + 1] = dp[i] + str1[i]
                elif len(dp[i + 1]) < len(new_dp[i]):
                    new_dp[i + 1] = new_dp[i]
            dp = new_dp
        (ans, i, j) = ('', 0, 0)
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
