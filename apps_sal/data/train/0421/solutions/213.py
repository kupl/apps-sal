class Solution:

    def lastSubstring(self, s: str) -> str:
        (i, j, k) = (0, 1, 0)
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = i + k + 1
            if i == j:
                j += 1
            k = 0
        return s[i:]
