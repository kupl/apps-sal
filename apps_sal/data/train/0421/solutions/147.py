class Solution:

    def lastSubstring(self, s: str) -> str:

        def helper(s):
            (p1, p2, prev_max_string) = (0, -1, None)
            for (i, l) in enumerate(s):
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
            return s[p1:]
        ans = helper(s)
        while len(s) > len(ans):
            (s, ans) = (ans, helper(ans))
        return s
