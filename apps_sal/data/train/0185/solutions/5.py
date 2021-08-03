class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        from itertools import permutations
        c = dict()
        count = 0
        for i in range(0, len(s) - k + 1):
            out = ''
            for j in range(i, i + k):
                out = out + s[j]
            if out not in c:
                c[out] = True
                count = count + 1
            if count == pow(2, k):
                return True
        return False
