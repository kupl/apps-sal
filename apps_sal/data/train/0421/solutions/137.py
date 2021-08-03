from collections import defaultdict


class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        max_string = None

        for i, c in enumerate(s):
            if c == max_char:
                new_string = s[i:]

                if max_string == None or new_string > max_string:
                    max_string = new_string

        return max_string
