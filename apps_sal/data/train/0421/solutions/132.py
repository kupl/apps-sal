class Solution:
    def lastSubstring(self, s: str) -> str:
        old = list(s)
        chars = list(s)
        chars.sort()
        index = old.index(chars[-1])
        indices = [i for i, x in enumerate(old) if x == chars[-1]]
        Max = s[indices[0]:]
        for i in range(len(indices)):
            Max = max(Max, s[indices[i]:])
        return Max
