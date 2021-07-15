class Solution:
    def lastSubstring(self, s: str) -> str:
        split = []
        cur = [s[0], 0]
        for i in range(1, len(s)):
            if ord(s[i]) > ord(s[i-1]):
                split.append(cur)
                cur = [s[i], i]
            else:
                cur[0] += s[i]
        split.append(cur)
        split = sorted(split, key=lambda x: x[0], reverse=True)
        return s[split[0][1]:]
