class Solution:

    def lastSubstring(self, s: str) -> str:
        (length, last, max_char) = (len(s), s[-1], s[-1])
        for i in range(length - 2, -1, -1):
            if s[i] < max_char:
                pass
            elif s[i] > max_char:
                last = s[i:]
                max_char = s[i]
            else:
                last = max(last, s[i:])
        return last
