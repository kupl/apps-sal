class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        l = [0] * 26
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            x = (ord(t[i]) - ord(s[i]) + 26) % 26
            if l[x] * 26 + x > k:
                return False
            l[x] += 1
        return True

