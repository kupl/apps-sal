class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            return False

        C = Counter()
        seen = set()
        for i in range(len(s)):
            if s[i] != t[i]:
                dist = (ord(t[i]) + 26 - ord(s[i])) % 26
                if dist not in C.keys():
                    C[dist] = 0
                else:
                    C[dist] += 1
                    dist += 26 * (C[dist])
                if dist > k:
                    return False
        return True
