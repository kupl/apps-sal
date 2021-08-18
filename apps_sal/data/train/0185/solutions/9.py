class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = len(s)
        r = set()
        target = 2 ** k
        for i in range(0, l - k + 1):
            r.add(
                s[i:i + k]
            )

            if len(r) == target:
                return True
        return False
