class Solution:
    def longestPrefix(self, s: str) -> str:
        len_s = len(s)
        nxts = [0] * len_s
        i = 1
        j = 0
        while i < len_s:
            while j > 0 and s[j] != s[i]:
                j = nxts[j - 1] # 退而求其次 考虑 s[:j - 1], 这个算过了是nxt(s[j - 1])
            if s[j] == s[i]: # while stop only two
                j = j + 1 
            nxts[i] = j
            i = i + 1
        return s[len_s-nxts[-1]:]

