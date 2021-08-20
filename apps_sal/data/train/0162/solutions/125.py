class Solution:

    def longestCommonSubsequence(self, s1, s2):

        def _longest_common_subsequence(s1, s2, cache):
            p = (len(s1), len(s2))
            if p in cache:
                return cache[p]
            elif len(s1) == 0 or len(s2) == 0:
                return 0
            elif s1[-1] == s2[-1]:
                answer = 1 + _longest_common_subsequence(s1[:-1], s2[:-1], cache)
                cache[p] = answer
                return answer
            else:
                answer = max(_longest_common_subsequence(s1, s2[:-1], cache), _longest_common_subsequence(s1[:-1], s2, cache))
                cache[p] = answer
                return answer
        return _longest_common_subsequence(s1, s2, {})
