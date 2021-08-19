class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        mem = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        return self.compute(mem, 0, 0, text1, text2)

    def compute(self, mem, ptr1, ptr2, text1, text2):
        if ptr1 == len(text1) or ptr2 == len(text2):
            return 0
        if mem[ptr1][ptr2] != -1:
            return mem[ptr1][ptr2]
        if text1[ptr1] == text2[ptr2]:
            ans = 1 + self.compute(mem, ptr1 + 1, ptr2 + 1, text1, text2)
            mem[ptr1][ptr2] = ans
            return ans
        else:
            ans = max(self.compute(mem, ptr1 + 1, ptr2, text1, text2), self.compute(mem, ptr1, ptr2 + 1, text1, text2))
            mem[ptr1][ptr2] = ans
            return ans
