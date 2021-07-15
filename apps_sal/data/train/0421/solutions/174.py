class Solution:
    def lastSubstring(self, s: str) -> str:
        char_list = set(list(s))
        char_list = list(char_list)
        char_list.sort()
        last_char = char_list[-1]
        max_string = last_char
        for index, char in enumerate(s):
            if char == last_char and max_string < s[index:]:
                max_string = s[index:]
        return max_string
    

