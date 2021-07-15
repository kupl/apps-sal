class Solution:
    def longestPrefix(self, s: str) -> str:
        len_s = len(s)
        nxts = [0]
        i = 1
        j = 0
        while i < len_s:
            while j > 0 and s[j] != s[i]:
                j = nxts[j - 1] # 退而求其次
            if s[j] == s[i]:
                j = j + 1
            else:
                j = 0
            i = i + 1
            nxts.append(j)
        return s[len_s-nxts[-1]:]

