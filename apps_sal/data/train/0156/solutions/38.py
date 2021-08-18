class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        longest_common_sub = ''
        str1_len = len(str1)
        str2_len = len(str2)
        dp = [[0 for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]
        for i in range(str1_len + 1):
            dp[i][0] = i
        for j in range(str2_len + 1):
            dp[0][j] = j
        for i in range(1, str1_len + 1):
            for j in range(1, str2_len + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        toret = []
        i = str1_len
        j = str2_len
        while i > 0 or j > 0:
            if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
                toret.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    toret.append(str1[i - 1])
                    i -= 1
                else:
                    toret.append(str2[j - 1])
                    j -= 1
        return ''.join(reversed(toret))
