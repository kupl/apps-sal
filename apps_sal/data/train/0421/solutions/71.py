class Solution:

    def lastSubstring(self, s: str) -> str:
        i = 0
        c = s[0]
        for num in range(len(s)):
            if s[num] > c:
                i = num
                c = s[num]
        j = i + 1
        k = 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j += k + 1
                k = 0
            else:
                i += k + 1
                j = i + 1
                k = 0
        return s[i:]
