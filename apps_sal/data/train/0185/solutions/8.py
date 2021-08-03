class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        check = []
        for kk in range(2**k):
            t = bin(kk)[2:]
            check.append('0' * (k - len(t)) + t)
        ss = set()
        for i in range(k, len(s) + 1):
            ss.add(s[i - k:i])
        for t in check:
            if t not in ss:
                return False
        return True
