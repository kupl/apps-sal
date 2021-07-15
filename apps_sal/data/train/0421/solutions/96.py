class Solution:
    def lastSubstring(self, s: str) -> str:
        # first store all the max chars in an array
        max_char = 'a'
        chars = []
        for i, char in enumerate(s):
            if char >= max_char:
                max_char = char
                chars.append(i)
        
        max_string = ''
        # now build the max substring from the chars array
        for idx in chars:
            if s[idx:] > max_string:
                max_string = s[idx:]
        return max_string
