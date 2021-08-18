class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        @params: two strings str1 and str2
        @return: shortest common supersequence
        '''
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                deletion = dp[i - 1][j]
                insertion = dp[i][j - 1]
                match = dp[i - 1][j - 1] + 1
                mismatch = dp[i - 1][j - 1]

                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = max(deletion, insertion, match)
                else:
                    dp[i][j] = max(deletion, insertion, mismatch)

        i, j = m, n
        ans = []

        while i > 0 or j > 0:
            if i == 0:
                ans.append(str2[j - 1])
                j -= 1

            elif j == 0:
                ans.append(str1[i - 1])
                i -= 1

            elif str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1

            elif dp[i][j] == dp[i - 1][j]:
                ans.append(str1[i - 1])
                i -= 1

            elif dp[i][j] == dp[i][j - 1]:
                ans.append(str2[j - 1])
                j -= 1

        return ''.join(reversed(ans))
