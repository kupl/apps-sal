class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        occ = {}
        for i in range(n):
            l = (ord(t[i]) - ord(s[i])) % 26
            if not l:
                continue
            try:
                if occ[l]:
                    occ[l] += 1
                    l = (occ[l] - 1) * 26 + l
                    if l > k:
                        return False
            except:
                if l > k:
                    return False
                occ[l] = 1

        return True
