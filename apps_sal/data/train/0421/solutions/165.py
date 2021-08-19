class Solution:

    def lastSubstring(self, s: str) -> str:
        maxchr = max(s)
        index = []
        maxstring = ''
        i = 0
        while i < len(s) and s[i:].find(maxchr) != -1:
            if i == 0 or s[i] != s[i - 1]:
                temp = s[i:].index(maxchr) + i
                index.append(temp)
                maxstring = max(maxstring, s[temp:])
                i = temp + 1
            else:
                i += 1
        return maxstring
