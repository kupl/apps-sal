class Solution:

    def lastSubstring(self, s: str) -> str:
        starts = list(range(len(s)))
        offset = 0
        while len(starts) > 1:
            newstarts = []
            end = max((s[start + offset] for start in starts if start + offset < len(s)))
            for (i, ch) in enumerate(starts):
                if i > 0 and starts[i - 1] + offset == starts[i]:
                    continue
                if ch + offset == len(s):
                    break
                if s[ch + offset] == end:
                    newstarts.append(ch)
            offset += 1
            starts = newstarts
        return s[starts[0]:]
