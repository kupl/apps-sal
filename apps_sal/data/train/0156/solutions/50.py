class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        @params: two strings str1 and str2
        @return: shortest common supersequence
        '''
        # Use Dynamic Programming to first compute shortest common subsequence
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: delete text1[i] in common subsequence
                deletion = dp[i - 1][j]
                # Case 2: delete text2[j] in common subsequence
                insertion = dp[i][j - 1]
                # Case 3: match --> common subsequence extend by 1
                match = dp[i - 1][j - 1] + 1
                # Case 4: mistch --> common subsequence keeps the same
                mismatch = dp[i - 1][j - 1]

                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = max(deletion, insertion, match)
                else:
                    dp[i][j] = max(deletion, insertion, mismatch)

        # Backtrack from dp[m][n] to construct shortest common supersequence
        # in revered order
        i, j = m, n
        ans = []

        while i > 0 or j > 0:
            # Case 1: str1 is used up
            if i == 0:
                ans.append(str2[j - 1])
                j -= 1

            # Case 2: str2 is used up
            elif j == 0:
                ans.append(str1[i - 1])
                i -= 1

            # Case 3: match
            elif str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1

            # Case 4: insertion of str1
            elif dp[i][j] == dp[i - 1][j]:
                ans.append(str1[i - 1])
                i -= 1

            # Case 5: deletion of str2
            elif dp[i][j] == dp[i][j - 1]:
                ans.append(str2[j - 1])
                j -= 1

            #print('i, j: ', i, j)
            # print(''.join(reversed(ans)))

        return ''.join(reversed(ans))
