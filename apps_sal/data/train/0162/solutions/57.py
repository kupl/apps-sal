class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     matrix = [[None]*(len(text2)+1) for i in range(len(text1)+1)]
    #     for j in range(len(text2)+1):
    #         matrix[0][j] = 0
    #     for i in range(len(text1)+1):
    #         matrix[i][0] = 0
    #     for i in range(1, len(text1)+1):
    #         for j in range(1, len(text2)+1):
    #             if text1[i-1] == text2[j-1]:
    #                 matrix[i][j] = 1 + matrix[i-1][j-1]
    #             else:
    #                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    #     return matrix[len(text1)][len(text2)]

    def longestCommonSubsequence(self, s1, s2):
        def _longest_common_subsequence(i, j, cache):
            p = (i, j)
            if p in cache:
                return cache[p]
            elif i < 0 or j < 0:
                return 0
            elif s1[i] == s2[j]:
                answer = 1 + _longest_common_subsequence(i - 1, j - 1, cache)
                cache[p] = answer
                return answer
            else:
                answer = max(_longest_common_subsequence(i, j - 1, cache), _longest_common_subsequence(i - 1, j, cache))
                cache[p] = answer
                return answer
        return _longest_common_subsequence(len(s1) - 1, len(s2) - 1, {})
