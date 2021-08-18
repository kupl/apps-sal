class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j = 0, 1
        ptr = 0

        while j + ptr < len(s):
            if s[i + ptr] == s[j + ptr]:
                ptr += 1
            elif s[i + ptr] < s[j + ptr]:
                i = j
                j += 1
                ptr = 0
            else:
                j += 1
                ptr = 0

        return s[i:]
