class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        prefix = [0] * n
        j, i = 0, 1
        while i < n:
            if s[j] == s[i]:
                j += 1
                prefix[i] = j
            elif j > 0:
                j = prefix[j - 1]
                i -= 1
            i += 1
        return s[:j]
