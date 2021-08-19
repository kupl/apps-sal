class Solution:

    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        maxx = 1
        start = 0
        for i in range(1, len(s)):
            if i - maxx >= 0 and s[i - maxx:i + 1] == s[i - maxx:i + 1][::-1]:
                start = i - maxx
                maxx += 1
            elif i - maxx >= 1 and s[i - maxx - 1:i + 1] == s[i - maxx - 1:i + 1][::-1]:
                start = i - maxx - 1
                maxx += 2
        return s[start:start + maxx]
