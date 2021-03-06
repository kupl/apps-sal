class Solution:

    def lastSubstring(self, s: str) -> str:
        c = max(s)
        a = []
        i = 0
        while i < len(s):
            if s[i] == c:
                a.append(i)
                while i < len(s) - 1 and s[i + 1] == c:
                    i += 1
            i += 1
        r = a[0]
        for i in a[1:]:
            if s[r:] < s[i:]:
                r = i
        return s[r:]
