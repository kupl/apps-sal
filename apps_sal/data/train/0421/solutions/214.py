class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        ans = 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                ans = i
                j = j + k + 1
                k = 0
            else:
                ans = j
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
        return s[ans:]
