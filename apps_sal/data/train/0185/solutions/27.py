class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = len(s)
        r = set()
        for i in range(0, l - k + 1):
            r.add(
                s[i:i + k]
            )
            if len(r) == 2**k:
                return True
        return False
