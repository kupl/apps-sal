class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, offset = 0, 1, 0

        while (i + offset < len(s)) and (j + offset < len(s)):
            if s[i + offset] == s[j + offset]:
                offset += 1
            else:
                if s[i + offset] < s[j + offset]:
                    i += offset + 1
                elif s[i + offset] > s[j + offset]:
                    j += offset + 1

                if i == j:
                    i += 1
                offset = 0
        loc = min(i, j)
        return s[loc:]
