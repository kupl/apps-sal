from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    current[j] = previous[j - 1] + 1
                else:
                    current[j] = max(current[j - 1], previous[j])
            previous = current
            current = [0] * (len(text1) + 1)
        return previous[-1]
