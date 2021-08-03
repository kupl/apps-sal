class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            ss = (bin(i)[2::]).zfill(k)
            if ss not in s:
                return False
        return True
