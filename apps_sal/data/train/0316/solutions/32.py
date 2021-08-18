class Solution:
    def longestPrefix(self, s: str) -> str:
        len_s = len(s)
        nxts = [0] * len_s
        i, j = 1, 0
        while i < len_s:
            while s[j] != s[i] and j > 0:
                j = nxts[j - 1]
            if s[j] == s[i]:
                j = j + 1
                nxts[i] = j
            i = i + 1
        return s[len_s - nxts[-1]:]
