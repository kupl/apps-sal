class Solution:

    def longestCommonSubsequence(self, s1, s2):
        def _longest_common_subsequence(i, j, cache):
            if i < 0 or j < 0:
                return 0
            elif cache[i][j] != None:
                return cache[i][j]
            elif s1[i] == s2[j]:
                answer = 1 + _longest_common_subsequence(i - 1, j - 1, cache)
                cache[i][j] = answer
                return answer
            else:
                answer = max(_longest_common_subsequence(i, j - 1, cache), _longest_common_subsequence(i - 1, j, cache))
                cache[i][j] = answer
                return answer
        return _longest_common_subsequence(len(s1) - 1, len(s2) - 1, [[None] * len(s2) for i in range(len(s1))])
