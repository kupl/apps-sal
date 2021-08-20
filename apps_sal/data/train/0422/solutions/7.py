class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        start = 0
        maxlength = 1
        for i in range(len(s)):
            if i - maxlength - 1 >= 0 and s[i - maxlength - 1:i + 1] == s[i - maxlength - 1:i + 1][::-1]:
                start = i - maxlength - 1
                maxlength += 2
            if i - maxlength >= 0 and s[i - maxlength:i + 1] == s[i - maxlength:i + 1][::-1]:
                start = i - maxlength
                maxlength += 1
        return s[start:start + maxlength]
