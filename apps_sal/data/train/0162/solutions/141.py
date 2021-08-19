class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0 for j in range(len(text2) + 1)]
        curr = [0 for j in range(len(text2) + 1)]
        for i in range(len(text1)):
            curr = [0 for j in range(len(text2) + 1)]
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    curr[j + 1] = prev[j] + 1
                else:
                    curr[j + 1] = max(prev[j + 1], curr[j])
            prev = curr
        return prev[len(text2)]
