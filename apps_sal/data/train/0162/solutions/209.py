class Solution:
    
    def _longest_common_subsequence(self, s1, s2, cache):
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        elif len(s1) == 0 or len(s2) == 0:
            cache[(s1, s2)] = 0
            return 0
        elif s1[-1] == s2[-1]:
            answer = 1 + self._longest_common_subsequence(s1[:-1], s2[:-1], cache)
            cache[(s1, s2)] = answer
            return answer
        else:
            answer = max(self._longest_common_subsequence(s1, s2[:-1], cache), self._longest_common_subsequence(s1[:-1], s2, cache))
            cache[(s1, s2)] = answer
            return answer
    
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        return self._longest_common_subsequence(s1, s2, {})
