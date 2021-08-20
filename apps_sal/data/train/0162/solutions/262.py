class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1:
            return 0
        l = len(text1)
        n = next((i for (i, c) in enumerate(text1) if c == text2[0]), l)
        commonSubstrings = [0] * n + [1] * (l - n)
        for c2 in text2[1:]:
            tmp = [0] * l
            tmp[0] = int(c2 == text1[0] or commonSubstrings[0])
            for (i, c1) in enumerate(text1[1:], 1):
                if c1 == c2:
                    tmp[i] = commonSubstrings[i - 1] + 1
                else:
                    tmp[i] = max(tmp[i - 1], commonSubstrings[i])
            commonSubstrings = tmp
        return commonSubstrings[-1]
