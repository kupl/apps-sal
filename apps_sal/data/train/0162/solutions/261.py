class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        lengthone = len(text1)
        lengthtwo = len(text2)

        n = 1000
        ans = [[0] * n for _ in range(n)]

        for i in range(lengthone):
            for j in range(lengthtwo):
                if text1[i] == text2[j]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])

        return ans[lengthone - 1][lengthtwo - 1]

#         if ans[len(text1)][len(text2)] != 0:
#             return ans[len(text1)][len(text2)]

#         elif len(text1) == 0 or len(text2) == 0:
#             return 0

#         elif text1[-1] == text2[-1]:
#             ans[len(text1)][len(text2)] = LCS(text1[:-1], text2[:-1]) + 1
#             return ans[len(text1)][len(text2)]

#         else:
#             ans[len(text1)][len(text2)] = max(
#                 LCS(text1[:-1], text2), LCS(text1, text2[:-1]))
#             return ans[len(text1)][len(text2)]


#         text1 = \"This code is a sample text for longest common subsequence\"
#         text2 = \"abcde\"

#         LCS(text1, text2)

#         print(\"LCS of {} and {} = {}\".format(text1, text2, LCS(text1, text2)))
