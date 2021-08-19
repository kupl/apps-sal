class Solution:

    def lastSubstring(self, s: str) -> str:

        def helper(s, start=0):
            (p1, p2) = (start, -1)
            for i in range(start + 1, len(s)):
                l = s[i]
                if p2 > 0:
                    if ord(l) > ord(s[p1 + i - p2]):
                        p1 = p2
                    elif ord(l) == ord(s[p1 + i - p2]):
                        pass
                    else:
                        p2 = -1
                elif ord(l) > ord(s[p1]):
                    p1 = i
                elif ord(l) < ord(s[p1]):
                    pass
                else:
                    p2 = i
            return p1
        (i, j) = (0, helper(s, 0))
        while j > i:
            (i, j) = (j, helper(s, j))
        return s[j:]
