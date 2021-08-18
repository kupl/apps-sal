class Solution:

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
