class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            diff = (ord(t[i]) - ord(s[i])) % 26
            if diff not in d:
                d[diff] = 1
            else:
                d[diff] += 1
            if 26 * (d[diff] - 1) + diff > k:
                return False
        return True
