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

        for i in product(['0', '1'], repeat=k):
            _ = ''.join(i)
            if _ not in r:
                return False
        return True
