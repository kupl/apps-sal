class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs_helper(index1, index2, memo={}):

            if index1 == len(text1) or index2 == len(text2):
                return 0
            key = (index1, index2)
            if key not in memo:

                if text1[index1] == text2[index2]:
                    memo[key] = 1 + lcs_helper(index1 + 1, index2 + 1, memo)
                else:
                    memo[key] = max(lcs_helper(index1, index2 + 1, memo),
                                    lcs_helper(index1 + 1, index2, memo))
            return memo[key]

        return lcs_helper(0, 0)
