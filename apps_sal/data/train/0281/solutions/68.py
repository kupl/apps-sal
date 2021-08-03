class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        i = 0
        j = defaultdict(int)
        print((len(s)))
        while i < len(s):
            mr = (ord(t[i]) - ord(s[i])) % 26
            if mr == 0:
                pass
            else:
                if mr + j.get(mr, 0) * 26 > k:
                    return False
                j[mr] += 1
            i += 1
        return True
