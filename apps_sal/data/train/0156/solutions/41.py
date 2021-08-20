class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        (M, N) = (len(str1), len(str2))
        dp = [[''] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
        LCS = dp[M][N]
        res = ''
        i = j = 0
        for c in LCS:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        res += str1[i:]
        res += str2[j:]
        return res
