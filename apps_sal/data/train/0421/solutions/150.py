class Solution:
    def lastSubstring(self, s: str) -> str:
        l = len(s)
        all_chars = set(list(s))
        all_chars = list(all_chars)
        all_chars.sort()
        mychar = all_chars[-1]
        max_sub = mychar
        for i, c in enumerate(s):
            if c == mychar:
                candidate = s[i:]
                if max_sub < candidate:
                    max_sub = candidate

        return max_sub
