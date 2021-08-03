class Solution:
    def longestPrefix(self, s: str) -> str:
        i = 0
        string = str()
        ans = 0
        j = len(s) - 1
        while i < len(s) - 1 and j > 0:
            if s[0:i + 1] == s[j:len(s)]:
                if i + 1 > ans:
                    ans = i + 1
                    string = s[0:i + 1]
            i = i + 1
            j = j - 1
        return string
