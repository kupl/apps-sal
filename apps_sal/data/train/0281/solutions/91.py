class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for i in range(len(s)):
            v = ord(t[i]) - ord(s[i])
            if v == 0:
                continue
            if v < 0:
                v += 26
            if v > k:
                return False
            if v in mp:
                high_v = mp[v] + 26
                if high_v > k:
                    return False
                mp[v] = high_v
            else:
                mp[v] = v
        return True
