class Solution:
    def lastSubstring(self, s: str) -> str:
        char_list = set(list(s))
        char_list = list(char_list)
        char_list.sort()
        char = char_list[-1]
        res = char
        for i,c in enumerate(s):
            if c == char:
                if res < s[i:]:
                    res = s[i:]
        return res
