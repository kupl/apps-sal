class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def _longest_common_subsequence(i, j):
            if i < 0 or j < 0:
                return 0
            
            if (i, j) not in mem:
                if text1[i] != text2[j]:
                    mem[(i, j)] = max(_longest_common_subsequence(i - 1, j), _longest_common_subsequence(i, j - 1))
                else:
                    mem[(i, j)] = _longest_common_subsequence(i - 1, j - 1) + 1
            
            return mem[(i, j)]
        
        mem = {}
        return _longest_common_subsequence(len(text1) - 1, len(text2) - 1)

