class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        maps = {}  # or maybe use array
        for i in range(len(s)):
            if s[i] != t[i]:
                diff = (ord(t[i]) - ord(s[i])) % 26
                if diff not in list(maps.keys()):
                    maps[diff] = 1
                else:
                    maps[diff] += 1
                if ((maps[diff] - 1) * 26 + diff) > k:
                    return False
        return True
