class Solution:

    def lastSubstring(self, s: str) -> str:
        max_char = 'a'
        chars = []
        for (i, char) in enumerate(s):
            if char >= max_char:
                max_char = char
                chars.append(i)
        max_string = ''
        for idx in chars:
            if s[idx:] > max_string:
                max_string = s[idx:]
        return max_string
