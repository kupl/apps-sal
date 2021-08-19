class Solution:

    def minCut(self, s):
        if not s:
            return 0
        if s == s[::-1]:
            return 0
        length = len(s)
        for i in range(1, length):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cut = [i for i in range(-1, length)]
        for i in range(length):
            (r1, r2) = (0, 0)
            while i - r1 >= 0 and i + r1 < len(s) and (s[i - r1] == s[i + r1]):
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            while i - r2 >= 0 and i + r2 + 1 < len(s) and (s[i - r2] == s[i + r2 + 1]):
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]
        '\n         :type s: str\n         :rtype: int\n         '
