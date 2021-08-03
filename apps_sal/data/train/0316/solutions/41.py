class Solution:
    def longestPrefix(self, s: str) -> str:
        i, j = 0, -1
        t = [0 for _ in range(len(s) + 1)]
        t[0] = -1
        while i < len(s):
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                t[i] = j
            else:
                j = t[j]
        return s[:t[-1]]
