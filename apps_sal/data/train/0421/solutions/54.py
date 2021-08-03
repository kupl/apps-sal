class Solution:
    def lastSubstring(self, s: str) -> str:
        max_letter = max(s)
        pre_letter = None

        current_max = max_letter
        for i, c in enumerate(s):
            if c == max_letter and pre_letter != c:
                current_max = max(current_max, s[i:])
            pre_letter = c

        return current_max
