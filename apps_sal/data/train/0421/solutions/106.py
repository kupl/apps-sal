class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = 'a'
        for char in s:
            if char > max_char:
                max_char = char

        compare = set()
        ret = max_char
        for i in range(len(s)):
            if s[i] == max_char:
                if s[i:] > ret:
                    ret = s[i:]

        return ret
