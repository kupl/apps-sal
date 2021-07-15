class Solution:
    def lastSubstring(self, s):
        i, j, inc = 0, 1, 0
        while j + inc < len(s):
          if s[i + inc] == s[j + inc]:
            inc += 1
          elif s[i + inc] > s[j + inc]:
            j += inc + 1
            inc = 0
          else:
            i = j
            j = i + 1
            inc = 0
        return s[i:]

