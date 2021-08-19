class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        (n1, n2) = (len(str1), len(str2))

        def lcs():
            dp = [[''] * (n2 + 1) for _ in range(n1 + 1)]
            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
            return dp[-1][-1]
        i = j = 0
        res = ''
        for ch in lcs():
            while i < n1 and str1[i] != ch:
                res += str1[i]
                i += 1
            while j < n2 and str2[j] != ch:
                res += str2[j]
                j += 1
            res += ch
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]
