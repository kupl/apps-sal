class Solution:

    def lastSubstring(self, s: str) -> str:
        (i, j, k) = (0, 1, 0)
        N = len(s)
        while j + k < N:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = i + k + 1
                j = i + 1
            k = 0
        return s[i:]
