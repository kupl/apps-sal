class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        h = [0] * 27
        for i in range(len(s)):
            c = ord(t[i]) - ord(s[i])
            if c == 0:
                continue
            if c < 0:
                c += 26
            h[c] += 1

        for i in range(1, len(h)):
            if i + (h[i] - 1) * 26 > k:
                return False

        return True
