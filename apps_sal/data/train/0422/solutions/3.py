class Solution:
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        max_len = 1
        end = 0
        for i in range(1, len(s)):
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                max_len = max_len + 1
                end = i
            elif i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                max_len = max_len + 2
                end = i
        return s[end - max_len + 1:end + 1]
