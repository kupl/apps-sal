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

    def _longest_common_subsequence(self, s1, s2, cache):
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        elif len(s1) == 0 or len(s2) == 0:
            return 0
        elif s1[-1] == s2[-1]:
            answer = 1 + self._longest_common_subsequence(s1[:-1], s2[:-1], cache)
            cache[(s1, s2)] = answer
            return answer
        else:
            answer = max(self._longest_common_subsequence(s1, s2[:-1], cache), self._longest_common_subsequence(s1[:-1], s2, cache))
            cache[(s1, s2)] = answer
            return answer

    def longestCommonSubsequence(self, s1, s2):
        return self._longest_common_subsequence(s1, s2, {})
