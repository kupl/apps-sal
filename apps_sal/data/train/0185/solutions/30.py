class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = set()
        required = 1 << k

        for i in range(len(s) - k + 1):
            if not s[i:i + k] in got:
                got.add(s[i:i + k])
                required -= 1
                if required == 0:
                    return True

        return False
