class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        for i in range(2**k):
            if bin(i)[2:].rjust(k, '0') not in s:
                return False
        return True
