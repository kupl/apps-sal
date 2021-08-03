class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        size1, size2 = len(str1), len(str2)
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        for i1 in range(1, size1 + 1):
            for i2 in range(1, size2 + 1):
                if str1[i1 - 1] == str2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
        i1, i2 = size1, size2
        res = []
        while i1 or i2:
            if i1 == 0:
                res.extend(reversed(str2[:i2]))
                break
            elif i2 == 0:
                res.extend(reversed(str1[:i1]))
                break
            elif str1[i1 - 1] == str2[i2 - 1]:
                res.append(str1[i1 - 1])
                i1 -= 1
                i2 -= 1
            elif dp[i1 - 1][i2] == dp[i1][i2]:
                res.append(str1[i1 - 1])
                i1 -= 1
            elif dp[i1][i2 - 1] == dp[i1][i2]:
                res.append(str2[i2 - 1])
                i2 -= 1
        return ''.join(reversed(res))
