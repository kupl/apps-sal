class Solution:

    def longestPrefix(self, s: str) -> str:
        len_s = len(s)
        nxts = [0] * len_s
        i = 1
        j = 0
        while i < len_s:
            while j > 0 and s[j] != s[i]:
                j = nxts[j - 1]
            if s[j] == s[i]:
                j = j + 1
            nxts[i] = j
            i = i + 1
        return s[len_s - nxts[-1]:]
