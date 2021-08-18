class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        mem = [[0] * len(text2) for _ in range(len(text1))]
        if text1[0] == text2[0]:
            mem[0][0] = 1
        for i in range(1, len(text1)):
            mem[i][0] = 1 if text1[i] == text2[0] else mem[i - 1][0]
        for i in range(1, len(text2)):
            mem[0][i] = 1 if text2[i] == text1[0] else mem[0][i - 1]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    mem[i][j] = max(mem[i - 1][j - 1] + 1, mem[i][j - 1], mem[i - 1][j])
                else:
                    mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])
        return mem[-1][-1]
