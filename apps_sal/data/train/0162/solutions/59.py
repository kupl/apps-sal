class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        mem1 = [0] * (len(text2) + 1)
        mem2 = [0] * (len(text2) + 1)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    mem2[j + 1] = mem1[j] + 1
                else:
                    mem2[j + 1] = max(mem2[j], mem1[j + 1])
            mem1 = mem2
            mem2 = [0] * (len(text2) + 1)
        return mem1[-1]
