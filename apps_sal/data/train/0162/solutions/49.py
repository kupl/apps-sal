class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if len(text2)>len(tex)

        memorize = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def LCS(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if memorize[i1][i2] != -1:
                return memorize[i1][i2]

            if text1[i1] == text2[i2]:
                memorize[i1][i2] = 1 + LCS(i1 + 1, i2 + 1)
            else:
                memorize[i1][i2] = max(LCS(i1, i2 + 1), LCS(i1 + 1, i2))
            return memorize[i1][i2]

        ans = LCS(0, 0)
        return ans
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # if len(text2)>len(tex)

#         memorize = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]
#         def LCS(i1, i2):
#             if i1 >= len(text1) or i2 >= len(text2): return 0

#             if memorize[i1+1][i2]==-1:
#                 memorize[i1+1][i2] = LCS(i1+1, i2)
#             option1 = memorize[i1+1][i2]


#             first_occurence = text2.find(text1[i1], i2)

#             if first_occurence != -1:
#                 if memorize[i1+1][i2+1]==-1:
#                     memorize[i1+1][first_occurence+1] = LCS(i1+1, first_occurence+1)
#                 option2 = 1 + memorize[i1+1][first_occurence+1]
#             else: option2 = 0


#             return max(option1, option2)
#         ans = LCS(0,0)
#         return ans
