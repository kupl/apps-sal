class Solution:

    def lastSubstring(self, s: str) -> str:
        best = 0
        n = len(s)
        for i in range(n):
            if s[i] > s[best]:
                best = i
            elif s[i] == s[best]:
                (idx1, idx2) = (best, i)
                while idx2 < n and s[idx1] == s[idx2]:
                    idx1 += 1
                    idx2 += 1
                if idx2 < n and s[idx2] > s[idx1]:
                    best = i
        return s[best:]

    def lastSubstring(self, s: str) -> str:
        (i, j, k) = (0, 1, 0)
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = j + (j - i) if i + k > j else j
                j = i + 1
            k = 0
        return s[i:]
