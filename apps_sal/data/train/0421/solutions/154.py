class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return s
        max_char = s[0]
        for c in s:
            if c > max_char:
                max_char = c
        largest = s
        (cur, prev) = (0, 0)
        for i in range(len(s)):
            if s[i] == max_char:
                if cur and s[cur:] > largest:
                    largest = s[cur:]
                cur = i
        if cur and s[cur:] > largest:
            largest = s[cur:]
        return largest
