class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        o = {}
        if len(s) != len(t):return False
        for i in range(len(s)):
            l = (ord(t[i]) -  ord(s[i]))%26
            if l == 0:continue
            if l > k :return False
            if l not in o :
                o[l] = l
            else:
                last = o[l]
                if last + 26 > k: return False
                o[l] = 26 + last
        return True

