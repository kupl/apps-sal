class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        dp = [[''] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
        lcs = dp[-1][-1]
        i = j = 0
        res = []
        for ch in lcs:
            while str1[i] != ch:
                res.append(str1[i])
                i += 1
            while str2[j] != ch:
                res.append(str2[j])
                j += 1
            res.append(ch)
            i += 1
            j += 1
        return ''.join(res) + str1[i:] + str2[j:]
