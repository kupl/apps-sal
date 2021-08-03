class Solution:
    def lastSubstring(self, s):
        i, j, inc = 0, 1, 0
        while j + inc < len(s):
            if i + inc == j:
                j = j + inc
                inc = 0
            elif s[j + inc] > s[i]:
                i = j + inc
                j = i + 1
                inc = 0
            elif s[i + inc] == s[j + inc]:
                inc += 1
            elif s[i + inc] < s[j + inc]:
                i = j
                j += 1
                inc = 0
            else:
                j += max(inc, 1)
                inc = 0
        return s[i:]
