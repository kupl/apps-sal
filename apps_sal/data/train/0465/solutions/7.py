class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                if cut[i + j + 1] > cut[i - j] + 1:
                    cut[i + j + 1] = cut[i - j] + 1
                j += 1
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                if cut[i + j + 2] > cut[i - j] + 1:
                    cut[i + j + 2] = cut[i - j] + 1
                j += 1
        return cut[-1]
